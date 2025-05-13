from pathlib import Path
from dataclasses import dataclass
from typing import Any, Union, Optional, List
from timeseries_inventory.utils.custom_logging import custom_logger
from timeseries_inventory.data_config.data_path_loader import DataPathLoader
from timeseries_inventory.data_config.data_stages_config import (
    DataIngestionConfig, 
    DataCleaningConfig, 
    DataValidationConfig, 
    DataTransformationConfig, 
    FeatureSelectionConfig, 
    FeatureEngineeringConfig, 
    ModelTrainingConfig, 
    ModelEvaluationConfig,
    ModelPredictionConfig
    )

class DataStagesManager: 
    """
    Manages access to YAML configuration using dot/bracket notation paths.
    Warps DataPathLoader to provide both raw and sectioned path access

    """
    
    def __init__(self, data_path: Optional[Union[str, List]]):
        self.logger = custom_logger()
        self._loader= DataPathLoader(data_path)
        self.yaml_data = self._loader.get_yaml_data()

  
    def data_ingestion_config(self) -> DataIngestionConfig:
        yaml_data = self._loader.data_ingestion
        return DataIngestionConfig(
            stage = yaml_data.stage,
            input = yaml_data.input,
            source = yaml_data.input.source,
            path = yaml_data.input.path,
            file_pattern = yaml_data.input.file_pattern,
            max_files = yaml_data.input.max_files,
            chunksize = yaml_data.input.chunksize,
            retry = yaml_data.retry,
            attempts = yaml_data.retry.attempts,
            delay_seconds = yaml_data.retry.delay_seconds
                 
        )


    def data_cleaning_config(self) -> DataCleaningConfig:
        yaml_data = self._loader.data_cleaning
        return DataCleaningConfig(
          stage = yaml_data.stage,
          operations = yaml_data.operations,    
          drop_duplicates = yaml_data.operations.drop_duplicates,
          fill_columns = yaml_data.operations.fill_columns
                
        )


    def data_validation_config(self) -> DataValidationConfig:
        yaml_data = self._loader.data_validation
        return DataValidationConfig(
            stage = yaml_data.stage,
            checks = yaml_data.checks,
            allow_nulls = yaml_data.checks.allow_nulls,
            fail_fast = yaml_data.checks.fail_fast,
            column_ranges = yaml_data.checks.column_ranges, 
            value = yaml_data.checks.column_ranges.value, 
            min = yaml_data.checks.column_ranges.value.min,
            max = yaml_data.checks.column_ranges.value.max
                      
        )


    def data_transformation_config(self) -> DataTransformationConfig:
        yaml_data = self._loader.data_transformation
        return DataTransformationConfig(
            stage = yaml_data.stage,
            transformations = yaml_data.transformations,
            output = yaml_data.output,
            directory = yaml_data.output.directory   
            
        )    


    def feature_selection_config(self) -> FeatureSelectionConfig:
        yaml_data = self._loader.feature_selection
        return FeatureSelectionConfig(
            stage = yaml_data.stage,
            strategy = yaml_data.strategy, 
            method = yaml_data.strategy.method,
            top_k = yaml_data.strategy.top_k,
            random_state =  yaml_data.strategy.random_stage,
            
        )   
    
    
    def feature_engineering_config(self) -> FeatureEngineeringConfig:
        yaml_data = self._loader.feature_engineering
        return FeatureEngineeringConfig(
            stage = yaml_data.stage, 
            operations = yaml_data.operations,
            generate_polynomials = yaml_data.operations.generate_polynomials,
            interaction_terms = yaml_data.operations.interaction_terms, 
            lag_features = yaml_data.operations.lag_features, 
            enabled = yaml_data.operations.lag_features.enabled, 
            lags = yaml_data.operations.lag_features.lags, 
            target_column = yaml_data.operations.lag_features.target_column
            
        ) 


    def model_training_config(self) -> ModelTrainingConfig:
        yaml_data = self._loader.model_training
        return ModelTrainingConfig(
            stage = yaml_data.stage, 
            model = yaml_data.model, 
            type = yaml_data.model.type, 
            hyperparameters=  yaml_data.model.hyperparameters,
            n_estimators = yaml_data.model.hyperparameters.n_estimators,
            max_depth = yaml_data.model.hyperparameters.max_depth,
            learning_rate = yaml_data.model.hyperparameters.learning_rate, 
            training = yaml_data.training,
            target_column = yaml_data.training.target_column,
            test_size = yaml_data.training.test_size, 
            random_state = yaml_data.training.random_state
            
        )
    
    
    def model_evaluation_config(self) -> ModelEvaluationConfig:
        yaml_data = self._loader.model_evaluation
        return ModelEvaluationConfig(
            stage = yaml_data.stage,
            evaluation =  yaml_data.evaluation,
            metric = yaml_data.evaluation.metric,
            cross_validation = yaml_data.evaluation.cross_validation,
            n_splits = yaml_data.evaluation.n_splits
            
            
        )    
        
        
    def model_prediction_config(self) -> ModelPredictionConfig:
        yaml_data = self._loader.model_prediction
        return ModelPredictionConfig(
            stage = yaml_data.stage,
            paths = yaml_data.paths, 
            model = yaml_data.paths.model, 
            input_data = yaml_data.paths.input_data,   
            output_predictions = yaml_data.paths.output_predictions,   
            settings = yaml_data.settings,        
            batch_size = yaml_data.settings.batch_size
              
        )  