from src.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.data_cleaning import DataCleaningPipeline
from src.pipeline.data_transformation import DataTransformationPipeline
from src.pipeline.data_training import DataTrainingPipeline
from src.pipeline.model_evaluation import ModelEvaluationPipeline


def test_DataIngestionTrainingPipeline():
        pipeline = DataIngestionTrainingPipeline()
        assert pipeline is not None  # simple existence check
        
        # maybe call a method and check result
        #result = pipeline.run()
        #assert result == expected_result

def test_DataCleaningPipeline():
        pipeline = DataCleaningPipeline()
        assert pipeline is not None  # simple existence check  


def test_DataTransformationPipeline():
        pipeline = DataTransformationPipeline()
        assert pipeline is not None  # simple existence check  


def test_DataTrainingPipeline():
        pipeline = DataTrainingPipeline()
        assert pipeline is not None  # simple existence check  


def test_ModelEvaluationPipeline():
        pipeline = ModelEvaluationPipeline()
        assert pipeline is not None  # simple existence check  