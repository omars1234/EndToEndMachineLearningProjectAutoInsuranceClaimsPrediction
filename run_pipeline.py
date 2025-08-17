from src.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.data_cleaning import DataCleaningPipeline
from src.pipeline.data_transformation import DataTransformationPipeline
from src.pipeline.data_training import DataTrainingPipeline
from src.pipeline.model_evaluation import ModelEvaluationPipeline


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


STAGE_NAME = "Data Transformation stage"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    print(f">>>>>> stage {STAGE_NAME} started ... <<<<<<")
    obj = DataTransformationPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    print(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e



STAGE_NAME = "Data Training stage"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    print(f">>>>>> stage {STAGE_NAME} started ... <<<<<<")
    obj = DataTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    print(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e



STAGE_NAME = "Model Evaluation stage"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    print(f">>>>>> stage {STAGE_NAME} started ... <<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    print(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e