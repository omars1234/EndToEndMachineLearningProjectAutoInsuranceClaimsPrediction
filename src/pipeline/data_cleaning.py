from src.config.configuration import DataCleaningManager
from src.components.data_cleaning import DataCleaning
import logging


STAGE_NAME = "Data Cleaning stage"

class DataCleaningPipeline:
    def __init__(self):
        pass

    def main(self):
        config=DataCleaningManager()
        config_create=config.create_directories()   
        data_cleaning=DataCleaning()
        create_data_cleaning=data_cleaning.clean_df()


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataCleaningPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e