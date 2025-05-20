# file_loader.py placeholder 
import time
import pandas as pd
from pathlib import Path
from typing import Optional, Dict, Iterator
from timeseries_inventory.utils.custom_logging import custom_logger
from timeseries_inventory.data_config.data_stages_config import DataIngestionConfig


class FileLoader:
    """
    Loads CSV files from the local source with validation, retry, and chunking support.
    
    Args: 
        config (DataIngestionConfig): Configuration object loaded from YAML
        read_args (dict, optional): Additional arguments fot 'pandas.read_csv'
        
    """
    
    def __init__(
        self, 
        config: DataIngestionConfig,
        read_args: Optional[Dict] = None
                 ):
       
        self.config = config
        self.read_args = read_args or {}
        self.logger = custom_logger()
        self._validate_directory()
    
    
    def _validate_directory(self):
        """Check if the directory exists and contains the matching files.""" 
        if not self.config.path.exists():
            raise FileNotFoundError(f"Directory does not exist: {self.config.path}")   
        self.match_files = list(self.config.path.glob(self.config.file_pattern))
        if not self.match_files:
            raise FileNotFoundError(f"No Files matching pattern '{self.config.file_pattern}' in {self.config.path}")
        self.logger.info(f"Found {len(self.match_files)} files matching pattern '{self.config.file_pattern}' in {self.config.path}")
    
    
    def load(self) -> Iterator[pd.DataFrame]:
        """
        Generator that yields chunks of data from the CSV files.
        
        Yields:
            pd.DataFrame: A chunk of the loaded data.
        """
        files = self.match_files[:self.config.max_files]
        
        for file in files:
            self.logger.info(f"Loading file: {file}")
            for attempt in range(1, self.config.retry['attempts'] + 1):
                try:
                    chunk_iter = pd.read_csv(
                        file, 
                        chunksize = self.config.chunksize, 
                        **self.read_args
                    )
                    for chunk in chunk_iter:
                        self.logger.debug(f"Yielding chunk of shape {chunk.shape} from {file.name}")
                        yield chunk
                    break    
                except Exception as e:
                    self.logger.warning(f"Failed to read {file.name} on attempt {attempt}/{self.config.retry['attempts']}: {e}")
                    if attempt < self.config.retry['attempts']:
                        time.sleep(self.config.retry['delay_seconds'])
                    else:
                        self.logger.error(f"Exceeded max retry attempts for file: {file.name}")
                        raise  
                      