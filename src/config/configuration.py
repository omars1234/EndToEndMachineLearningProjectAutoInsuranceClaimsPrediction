
import os
from constants.main import *
from src.entity.config_entity import (DataIngestionConfig)



class DataIngestionManager:
    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        self.data_ingestion_config = data_ingestion_config

    def create_directories(self):
        os.makedirs(self.data_ingestion_config.data_artifacts_dir,exist_ok=True)
        os.makedirs(self.data_ingestion_config.data_ingested_dir,exist_ok=True) 