import joblib
from pathlib import Path
import numpy as np
from constants.main import *
import pandas as pd
from requests import request

class PredictionPipeline:
    def __init__(self):
        self.preprocessor = joblib.load(Path('saved_preproccesor\preprocessor.joblib'))
        self.model=joblib.load(Path('saved_model\model.joblib'))

    def predict(self,input_data):


        preprocessed_data=self.preprocessor.transform(input_data)
        prediction=self.model.predict(preprocessed_data)
        prediction_prob=self.model.predict_proba(preprocessed_data)
        prediction_prob=np.round(prediction_prob,4)
        
        if prediction==0:
            return "No Claims with probability {}".format(prediction_prob)
        else:
            return "With Claims with probability {}".format(prediction_prob)
        
    
