from Phishing.exception import My_Exception
from datetime import datetime
import os,sys 

Data_SET_PATH = os.path.join("D:\FSDS PROJECT\Project1_\data\dataset_full.csv")
TRAIN_FILE = "Train.csv"
TEST_FILE = "Test.csv"

class traning_pipeline_config():
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(), "artifact" , f"{datetime.now().strftime('%d%m%y %H%M%S')}")
        except Exception as e:
            raise My_Exception(e,sys)


class DataIngestionConfig():
    def __init__(self,traning_pipeline_config:traning_pipeline_config):
        try:
            self.DataBase_Path = Data_SET_PATH
            self.Data_Ingestion_Dir = os.path.join(traning_pipeline_config.artifact_dir,"Data_Ingestion")
            self.Train_File_Path = os.path.join(self.Data_Ingestion_Dir,"dataset",TRAIN_FILE)
            self.Test_File_Path = os.path.join(self.Data_Ingestion_Dir,"dataset",TEST_FILE)
            self.test_size = 0.3
        except Exception as e:
            raise My_Exception(e,sys)
        