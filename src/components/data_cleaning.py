import os
import yaml
import pandas as pd
import numpy as np
from constants.main import *
from src.config.configuration import DataCleaningConfig


class DataCleaning:
    def __init__(self,data_cleaning_config:DataCleaningConfig=DataCleaningConfig()):
        """
        :param data_ingestion_config: configuration for data ingestion
        """
        self.data_cleaning_config = data_cleaning_config   
        with open(self.data_cleaning_config.schema_file_path_dir) as yaml_file:
             schema = yaml.safe_load(yaml_file)
        self.schema_config=(schema)
        
        
    def clean_df(self):

        df=pd.read_csv(self.data_cleaning_config.raw_data_file_path_dir)
        
        columns_veh_value_validate = self.schema_config["col_veh_value_validate"]
        columns_to_drop=self.schema_config["cols_to_drop"]
        
        

        df=df.drop(columns_to_drop,axis=1)
        df=df[df["veh_value"] != 0]
        df["veh_value"]=df["veh_value"]*10000
        df=df.rename(columns={'clm': 'Claim_recorded',
                            'numclaims': 'number_of_Recorded_claims',
                            'claimcst0':'Claims_cost',
                            'agecat':'age_category'
                            })

        df.columns=df.columns.str.capitalize()  

        df.to_csv(os.path.join(self.data_cleaning_config.cleaned_data_ingested_dir,CLEANED_DATA_FILE_DIR_NAME),index=False,header=True)