# Here will be the yaml loader logic

import yaml
from pathlib import Path
from typing import Any, Optional, Union, Dict
from timeseries_inventory.utils.custom_logging import custom_logger


class DataPathLoader:
    """
    Loads a YAML file and extracts all key paths as strings.
    Handles nested dictionaries and lists, returning a flat list of keys
    using dot and bracket notation.
    """
    
    def __init__(
        self, 
        data_path:Optional[Union[str, Path]] = None
        ):
        self.logger = custom_logger()
        if data_path:
            self.data_path = Path(data_path) 
        else:
            self.data_path = Path(__file__).parent / "data_path.yaml"
            self.logger.info(f"No path provided. Using default: {self.data_path}")


    def _load_yaml(self) -> dict:
        if not self.data_path.exists():
            self.logger.error(f"YAML file not found: {self.data_path}")
            raise FileNotFoundError(f"YAML file not found: {self.data_path}")
        try:
            with self.data_path.open("r", encoding="utf-8") as f:
                yaml_data = yaml.safe_load(f) or {}
                self.logger.info(f"Successfully loaded YAML file from {self.data_path}")
        except yaml.YAMLError as e:
            self.logger.exception(f"Failed to parse YAML")
            raise ValueError(f"Error parsing YAML data path: {e}")
        # return yaml_data  
        return self._convert_paths(yaml_data)  
    
    def _convert_paths(self, data: Any) -> Any:
        """
        Recursively convert 'path' keys to Path objects where the value is a string.
        """
        if isinstance(data, dict):
            new_data = {}
            for k, v in data.items():
                if k == 'path' and isinstance(v, str):
                    new_data[k] = Path(v)
                else:
                    new_data[k] = self._convert_paths(v) 
            return new_data
        elif isinstance(data, list):
            return [self._convert_paths(item) for item in data]
        return data
    
    
    def get_yaml_data(self) -> Dict: 
        return self._load_yaml()
