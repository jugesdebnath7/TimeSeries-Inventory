# loader.py placeholder 

from pathlib import Path
from dataclasses import dataclass
from typing import Any, Union, Optional, List, Dict
from timeseries_inventory.utils.custom_logging import custom_logger
from timeseries_inventory.data_config.data_path_loader import DataPathLoader


"""
Manages access to YAML configuration using dot/bracket notation paths.
Warps DataPathLoader to provide both raw and sectioned path access

""" 

__all__ = [
    
    "DataIngestionConfig",
    "DataCleaningConfig",
    "DataValidationConfig",
    "DataTransformationConfig",
    "FeatureSelectionConfig",
    "FeatureEngineeringConfig",
    "ModelTrainingConfig",
    "ModelEvaluationConfig",
    "ModelPredictionConfig"
]

  
@dataclass(frozen=True)
class DataIngestionConfig:
    stage: str
    input: Dict[str, Union[str, int]]
    source: str
    path: str
    file_pattern: str
    max_files: int
    chunksize: int
    retry: Dict[str, int]
    attempts: int
    delay_seconds: int


@dataclass(frozen=True)
class DataCleaningConfig:
    stage: str
    operations: Dict[str, Union[bool, List[str]]]    
    drop_duplicates: bool
    fill_columns: List[str]


@dataclass(frozen=True)
class DataValidationConfig:
    stage: str
    checks: Dict[str, Union[bool, Dict[str, Dict[str, int]]]]
    allow_nulls: bool
    fail_fast: bool
    column_ranges: Dict[str, Dict[str, int]]
    value: str
    min: int
    max: int


@dataclass(frozen=True)
class DataTransformationConfig:
    stage: str
    transformations: Dict[str, Any]
    output: Dict[str, str]
    directory: str


@dataclass(frozen=True)
class FeatureSelectionConfig:
    stage: str
    strategy: Dict[str, Union[str, int]]
    method: str
    top_k: int
    random_state: int


@dataclass(frozen=True)
class FeatureEngineeringConfig:
    stage: str 
    operations: Dict[str, Union[bool, Dict[str, Union[bool, List[int], str]]]]
    generate_polynomials: bool
    interaction_terms: bool
    lag_features: Dict[str, Union[bool, List[int], str]]
    enabled: bool
    lags: List[int]
    target_column: str


@dataclass(frozen=True)
class ModelTrainingConfig:
    stage: str
    model: Dict[str, Union[List[str], Dict[str, Union[int, float]]]]
    type: List[str]
    hyperparameters: Dict[str, Union[int, float]]
    n_estimators: int
    max_depth: int
    learning_rate: float
    training: Dict[str, Union[str, float, int]]
    target_column: str
    test_size: float
    random_state: int


@dataclass(frozen=True)
class ModelEvaluationConfig:
    stage: str
    evaluation: Dict[str, Union[str, bool, int]]
    metric: str
    cross_validation: bool
    n_splits: int
    

@dataclass(frozen=True)
class ModelPredictionConfig:
    stage: str
    paths: Dict[str, str]
    model: str
    input_data: str  
    output_predictions: str
    settings: Dict[str, int]
    batch_size: int



