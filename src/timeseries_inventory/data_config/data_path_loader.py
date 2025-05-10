# Here will be the yaml loader logic

import yaml
from pathlib import Path
from typing import Any, Optional, List, Union
from timeseries_inventory.utils.custom_logging import custom_logger


class DataPathLoader:
    """
    Loads a YAML file and extracts all key paths as strings.
    Handles nested dictionaries and lists, returning a flat list of keys
    using dot and bracket notation.
    """
    
    def __init__(self, 
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
            self.logger.exception(f"Fail to parse YAML")
            raise ValueError(f"Error parsing YAML data path: {e}")
        return yaml_data    
    
    
    def _extract_keys(self, data:Any, parent_key:str = "") -> List[str]:
        """
        Recursively extracts all key paths from a nested dictionary or list.
        """
        keys = []
        if isinstance(data, dict):
            for k, v in data.items():
                full_key = f"{parent_key}.{k}" if parent_key else k
                keys.append(full_key)
                keys.extend(self._extract_keys(v, full_key))  # Recurse if value is a dict
        elif isinstance(data, list):
            for idx, item in enumerate(data):
                full_key = f"{parent_key}[{idx}]"
                keys.append(full_key)
                keys.extend(self._extract_keys(item, full_key)) # Recurse if item is a dict or list
        return keys


    def get_yaml_data(self) -> List[str]:
        yaml_data_path = self._load_yaml()
        return self._extract_keys(yaml_data_path)
