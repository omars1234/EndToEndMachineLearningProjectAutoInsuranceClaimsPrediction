import pandas as pd
import numpy as np
from pathlib import Path
import yaml
from box import ConfigBox
import os
from dataclasses import dataclass
from datetime import datetime
from constants.main import *
from MongoDBConfig.main import *



TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP

training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:

    DB_NAME :Path=DB_NAME
    COLLECTION_NAME:str=COLLECTION_NAME
    CONNECTION_URL:str=CONNECTION_URL
    data_artifacts_dir:str=ARTIFACT_DIR
    data_ingested_dir:str=os.path.join(training_pipeline_config.artifact_dir,DATA_INGESTED_DIR_NAME)


@dataclass
class DataCleaningConfig:
    raw_data_file_path_dir :str=os.path.join(training_pipeline_config.artifact_dir,DATA_INGESTED_DIR_NAME,RAW_DATA_FILE_PATH_DIR_NAME)
    cleaned_data_ingested_dir:str=os.path.join(training_pipeline_config.artifact_dir,CLEANED_DATA_INGESTED_DIR_NAME)
    schema_file_path_dir:str=SCHEMA_FILE_PATH
        