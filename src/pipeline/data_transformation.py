from src.components.data_transformation import DataTransformation
from src.config.configuration import DataTransformationManager
import logging

STAGE_NAME = "Data Transformation stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=DataTransformationManager()
        config.create_directories()
        data_transformation=DataTransformation()
        data_transformation.transform_df()


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e