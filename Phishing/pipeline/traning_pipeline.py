from Phishing.components.data_ingestion import DataIngestion
from Phishing.exception import My_Exception
from Phishing.logger import logging
from Phishing.entity import config_entity
import sys

def Start_traning_pipeline():
    try:
        traning_pipeline_config = config_entity.traning_pipeline_config()
        data_ingestion_config = config_entity.DataIngestionConfig(traning_pipeline_config=traning_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.inicate_data_ingestion()
        print(data_ingestion_artifact)
    

    except Exception as e:
        raise My_Exception(e,sys)