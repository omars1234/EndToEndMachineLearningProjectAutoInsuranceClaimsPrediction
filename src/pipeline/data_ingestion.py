from src.config.configuration import DataIngestionManager
from src.components.data_ingestion import DataIngestion
import logging


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=DataIngestionManager()
        config_create=config.create_directories()
        data_ingestion=DataIngestion()
        create_data_ingestion=data_ingestion.export_data_into_feature_store()


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e