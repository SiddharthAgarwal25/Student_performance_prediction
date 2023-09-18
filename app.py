from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import PredictPipeline, CustomData
from sklearn.preprocessing import StandardScaler
from src.logger import logging

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')

    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )

        dataframe = data.get_data_as_data_frame()
        logging.info("Data caught and dataframe created...")

        prediction = PredictPipeline()
        logging.info("Starting prediction ... ")
        y_pred = prediction.predict(dataframe)
        logging.info("prediction complete..")
        return render_template('home.html', results=y_pred[0])


if __name__=="__main__":
    app.run(host="0.0.0.0")        