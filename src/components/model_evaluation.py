from src.config.configuration import ModelEvaluationConfig
from src.components.data_training import DataTraining
import joblib
import os
from constants.main import *
import numpy as np

from sklearn.metrics import confusion_matrix,f1_score,accuracy_score,classification_report,auc,roc_curve
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
import json

class DataEvaluation:
    def __init__(self,model_evaluation_config:ModelEvaluationConfig=ModelEvaluationConfig()):
        """
        :param data_ingestion_config: configuration for data ingestion
        """
        self.model_evaluation_config = model_evaluation_config
 
        
    def evaluation(self):
        _,_,X_train, X_test, y_train, y_test=DataTraining().trainig()
        model=joblib.load(self.model_evaluation_config.model_dir)

        scoring = {
            'f1': 'f1_macro'
        }   
      
        cv_results = cross_validate(model, X_train, y_train, cv=CROSS_VALIDATION_CV, scoring=scoring)
        CV_results_summary={"test_f1": cv_results['test_f1'].mean()}

        #rmse_scores = -neg_rmse_scores
        #rmse_scores= np.round(rmse_scores, 2)
        #mean_rmse_scores= round(rmse_scores.mean(), 2)

        #CV_results={"rmse_CV_scores":rmse_scores.tolist(),"mean_rmse_scores":mean_rmse_scores,"std_rmse_scores":std_rmse_scores,
        #            "Standard_Error_SE":Standard_Error_SE,"ci":ci}

        prediction=model.predict(X_test)
        f1=f1_score(y_test,prediction)
        accuracy=accuracy_score(y_test,prediction)

        y_pred_proba = model.predict_proba(X_test)[:, 1]
        fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
        roc_auc = auc(fpr, tpr)


        #cm=confusion_matrix(y_test,prediction)
        

        scores=[{'accuracy':accuracy,"f1 score":f1,"roc_auc":roc_auc,'CV_results_summary':CV_results_summary}]

        #all_results_dict=[CV_results,scores]
        with open(os.path.join(self.model_evaluation_config.evaluation_file_dir,EVALUATION_FILE_DIR_NAME), "w") as f:
            json.dump(scores,f,indent=4)