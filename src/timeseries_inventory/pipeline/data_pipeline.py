from timeseries_inventory.data_config.data_stages_manager import DataStagesManager
from timeseries_inventory.utils.custom_logging import custom_logger
from timeseries_inventory.ingestion.file_loader import FileLoader


class DataStagesPipeline:
    def __init__(self):
        self._data_stages_manager = DataStagesManager()
        

class DataIngestionPipeline:
    def __init__(self, data_pipeline: DataStagesPipeline):
        self._data_ingestion = self._dat
    
    
    def data_ingestion_pipeline(self):
        pass



class DataCleaningPipeline:
    def __init__(self):
        pass
    
    
    def data_cleaning_pipeline(self):
        pass
    
    
    
class DataValidationPipeline:    
    def __init__(self):
        pass
    
    
    def data_validation_pipeline(self):
        pass
  
    
class DataTransformationPipeline: 
    def __init__(self):
        pass
    
    
    def data_transformation_pipeline(self):
        pass
    
    
class FeatureSelectionPipeline:       
    def __init__(self):
        pass
    
    
    def feature_selection_pipeline(self):
        pass
    
    
class FeatureEngineeringPipeline: 
    def __init__(self):
        pass
    
    
    def feature_engineering_pipeline(self):
        pass
   
    
class ModelTrainingPipeline:   
    def __init__(self):
        pass
    
    
    def model_training_pipeline(self):
        pass


class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    
    def model_evaluation_pipeline(self):
        pass
   
    
class ModelPredictionPipeline:    
    def __init__(self):
        pass    
    
    
    def model_prediction_pipeline(self):
        pass    