from flask import Flask,render_template,request
from src.pipeline.data_prediction import PredictionPipeline
import os
import pandas as pd

#from requests import request


app=Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return render_template('index2.html') 


@app.route('/train',methods=["GET"])
def training():
    os.system("python run_pipeline.py")
    return ("Training Successful")


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            data = request.get_json()  # <-- JSON from fetch

            Veh_value = float(data['Veh_value'])
            Exposure = float(data['Exposure'])
            Claims_cost = float(data['Claims_cost'])
            Veh_body = str(data['Veh_body'])
            Veh_age = int(data['Veh_age'])
            Gender = str(data['Gender'])
            Area = str(data['Area'])
            Age_category = int(data['Age_category'])

            
            input_data = pd.DataFrame({
                                        "Veh_value": [Veh_value],
                                        "Exposure": [Exposure],
                                        "Claims_cost": [Claims_cost],
                                        "Veh_body": [Veh_body],
                                        "Veh_age": [Veh_age],
                                        "Gender": [Gender],
                                        "Area": [Area],
                                        "Age_category": [Age_category],

                                    })


            obj = PredictionPipeline()
            predict = obj.predict(input_data)
            
            return {"prediction": str(predict), "details": None}
    

        except Exception as e:
            print('Exception:', e)
            return {"error": str(e)}, 400
        
    else:
        return render_template('results.html')        
       

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)