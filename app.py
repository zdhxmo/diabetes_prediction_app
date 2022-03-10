import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle
from joblib import load

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    scaler = load('./model/scaler.joblib')
    model = load('./model/model.joblib')

    features_input = [float(x) for x in request.form.values()]
    feats = ['Glucose', 'Insulin', 'BMI', 'Age']

    df = pd.DataFrame([features_input], columns=feats)
    X = scaler.transform(df)
    predict_features = pd.DataFrame(X, columns=feats)

    model_prediction = model.predict(predict_features)

    return render_template('result.html', prediction=model_prediction)


if __name__ == "___main__":
    app.run(debug=True)
