from flask import Flask,render_template,jsonify,Request
import numpy as np
from src.pipeline.data_prediction import PredictionPipeline
import os
import pandas as pd
import joblib
from requests import request


app=Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return render_template('index.html') 


@app.route('/train',methods=["GET"])
def training():
    os.system("python run_pipeline.py")
    return ("Training Successful")


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            Veh_value=float(request.form['Veh_value'])
            Exposure=float(request.form['Exposure'])
            Number_of_recorded_claims=str(request.form['Number_of_recorded_claims'])
            Claims_cost=float(request.form['Claims_cost'])
            Veh_body=str(request.form['Veh_body'])
            Veh_age=str(request.form['Veh_age'])
            Gender=str(request.form['Gender'])
            Area=str(request.form['Area'])
            Age_category=str(request.form['Age_category'])

            
            input_data = pd.DataFrame({
                                        "Veh_value": [Veh_value],
                                        "Exposure": [Exposure],
                                        "Number_of_recorded_claims": [Number_of_recorded_claims],
                                        "Claims_cost": [Claims_cost],
                                        "Veh_body": [Veh_body],
                                        "Veh_age": [Veh_age],
                                        "Gender": [Gender],
                                        "Area": [Area],
                                        "Age_category": [Age_category],

                                    })


            obj = PredictionPipeline()
            predict = obj.predict(input_data)

            
            return render_template('results.html', prediction = predict)
    

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
        
    else:
        return render_template('results.html')        
       

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)