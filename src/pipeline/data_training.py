from src.config.configuration import DataTrainingManager
from src.components.data_training import DataTraining
import logging


STAGE_NAME = "Data Training stage"

class DataTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=DataTrainingManager()
        config.create_directories()   
        data_cleaning=DataTraining()
        data_cleaning.trainig()



if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e