import sys
from src.configuration.mongodb_connection import MongoDBClient
from src.exception import SensorException
import os,sys
from src.logger import logging
from src.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from src.pipeline.training_pipeline import TrainingPipeline

if __name__ == "__main__":
    try:
        training_pipeline = TrainingPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
    
    
    """
    training_pipeline_config = TrainingPipelineConfig()
    date_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    print(date_ingestion_config.__dict__)
    """