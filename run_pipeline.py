from src.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.data_cleaning import DataCleaningPipeline

import logging


STAGE_NAME = "Data Ingestion stage"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    print(f">>>>>> stage {STAGE_NAME} started ... <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    print(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Data Cleaning stage"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    print(f">>>>>> stage {STAGE_NAME} started ... <<<<<<")
    obj = DataCleaningPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    print(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e