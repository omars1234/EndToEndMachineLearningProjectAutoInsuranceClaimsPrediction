from pathlib import Path
import os
from datetime import date
from MongoDBConfig.main import *


"""
General related constant 
"""
SCHEMA_FILE_PATH = Path(r"schema.yaml")
SCHEMA_CLAENED_FILE_PATH = Path(r"cleaned_schema.yaml")


DB_NAME= DB_NAME
COLLECTION_NAME=COLLECTION_NAME
CONNECTION_URL=CONNECTION_URL


"""
Data Ingestion related constant 
"""
ARTIFACT_DIR: str = "artifact"
DATA_INGESTED_DIR_NAME: str = "01_ingested_data"
RAW_DATA_FILE_PATH_DIR_NAME : str = "raw_data.csv"


"""
Data Cleaning related constant
"""
CLEANED_DATA_INGESTED_DIR_NAME : str = "02_ingested_cleaned_data"
CLEANED_DATA_FILE_DIR_NAME :str = "cleaned_data.csv"



"""
Data Transformation related constant
"""
PREPROCCESOR_TRANSFORMATION_OBJECt_DIR :str='saved_preproccesor'
PREPROCCESOR_TRANSFORMATION_OBJECt_DIR_NAME='preprocessor.joblib'



"""
Data Training related constant
"""
MODEL_DIR='saved_model'
MODEL_DIR_NAME='model.joblib'
TARGER_FEATURE :str = "Claim_recorded"
TEST_SPLIT_RATIO: float = 0.3
RANDOM_STATE : int = 42



"""
Data Evaluation related constant
"""
EVALUATION_FILE_DIR='evaluation_file'
EVALUATION_FILE_DIR_NAME='scores.json'
CROSS_VALIDATION_CV :int = 5