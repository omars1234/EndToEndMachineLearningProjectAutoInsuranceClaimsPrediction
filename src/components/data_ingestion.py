from src.entity.config_entity import DataIngestionConfig
import pandas as pd
import os
from constants.main import *
import pymongo


class DataIngestion:
    def __init__(self,ingestion_config:DataIngestionConfig=DataIngestionConfig()):

        self.ingestion_config = ingestion_config
 
        
    def export_data_into_feature_store(self):

        client=pymongo.MongoClient(self.ingestion_config.CONNECTION_URL)
        data_base=client[self.ingestion_config.DB_NAME]
        collection=data_base[self.ingestion_config.COLLECTION_NAME]

        df=pd.DataFrame(collection.find())
        df=df.drop("_id",axis=1)
        
        df.to_csv(os.path.join(self.ingestion_config.data_ingested_dir,RAW_DATA_FILE_PATH_DIR_NAME),index=False,header=True)