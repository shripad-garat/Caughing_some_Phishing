from Phishing.entity.artifact_entity import DataIngestionArtifact
from Phishing.entity.config_entity import DataIngestionConfig
from Phishing.logger import logging
from Phishing.exception import My_Exception
from Phishing.utils import main_utils
from sklearn.model_selection import train_test_split
import pandas as pd 
import os,sys


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise My_Exception(e,sys)
        
    def inicate_data_ingestion(self):
        try:
            logging.info("Inicating the Data ingestion")
            logging.info("Loading the data set from local data folder")
            data = pd.read_csv(self.data_ingestion_config.DataBase_Path)
            data.drop_duplicates(inplace=True)
            logging.info("Spliuting the data into train and test datasets")
            train_data,test_data = train_test_split(data,test_size=self.data_ingestion_config.test_size,random_state=100)
            logging.info("Saving the train and test data into data set dir in artifact dir")
            data_dir = os.path.dirname(self.data_ingestion_config.Train_File_Path)
            os.makedirs(data_dir,exist_ok=True)
            train_data.to_csv(self.data_ingestion_config.Train_File_Path,index=False,header=True)
            test_data.to_csv(self.data_ingestion_config.Test_File_Path,index=False,header=True)
            logging.info("Complated the Data ingestion pipeline preparing the artifact")
            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.Train_File_Path,
                test_file_path = self.data_ingestion_config.Test_File_Path,
                base_data_path = self.data_ingestion_config.DataBase_Path
            )
            return data_ingestion_artifact
        except Exception as e:
            raise My_Exception(e,sys)