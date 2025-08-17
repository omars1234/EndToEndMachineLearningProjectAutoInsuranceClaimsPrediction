from src.config.configuration import ModelEvaluationManager
from src.components.model_evaluation import DataEvaluation
import logging


STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ModelEvaluationManager()
        config.create_directories()   
        data_cleaning=DataEvaluation()
        data_cleaning.evaluation()



if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e