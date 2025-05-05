# logger.py placeholder 
import os
import logging
from logging.handlers import RotatingFileHandler


def logger_config(
        log_file="ml_model.log",
        log_level=logging.INFO, 
        base_dir=None, 
        logger_name: str = "ML_Logger"):
    """
    Setup a rotating logger.

    Args:
        log_file (str): Name of the log file.
        log_level (str): logging level as a string (e.g.: INFO, DEBUG). 
        base_dir (str) =  Base directory for artifacts (default to ./artifacts)
    
    Returns:
        logging.Logger: Configured logger instance    
    
    """
    # Determine the base firectory
    if base_dir is None:
        base_dir = os.path.join(os.getcwd(), "../artifacts")

    # Ensure log sub directories exists
    log_directory = os.path.join(base_dir, "logs")
    os.makedirs(log_directory, exist_ok=True)

    # Full path of the log file
    log_file_path = os.path.join(log_directory, log_file)

    # Convert string level to numeric logging level
    log_level = getattr(logging, log_level.upper(), logging.INFO)

    # Create custom logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    # Avoid duplicate handler if this function is called multiple times
    if not logger.handlers:
        log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        logger.addHandler(console_handler)

        # Rotating file handler
        file_handler = RotatingFileHandler(log_file_path, maxBytes=5*1024*1024, backupCount=5)
        file_handler.setFormatter(log_formatter)
        logger.addHandler(file_handler)

    return logger    


