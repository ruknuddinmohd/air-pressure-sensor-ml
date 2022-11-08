import sys
from telnetlib import SE
from src.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig
from src.exception import SensorException
from src.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
import sys,os
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation

class TrainingPipeline:

    def __init__(self):
        self.training_pipeline = TrainingPipelineConfig()
        #
        #self.training_pipeline_config = training_pipeline

    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Starting data ingestion")
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline)
            date_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = date_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed successfully and artifact :{data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e,sys)

    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)-> DataValidationArtifact:
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                                    data_validation_config=data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
        except Exception as e:
            raise SensorException(e,sys)

    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)

    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)

    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)

    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)

    def run_pipeline(self):
        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
        except Exception as e:
            raise SensorException(e,sys)
