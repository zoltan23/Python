import numpy as numpy
from flask import Flask, request, render_template
import pickle
from NLP_KNN import cv, cleanData

app = Flask(__name__)
model = pickle.load(open('model_knn.pkl', 'rb'))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    new_data = cleanData(int_features)
    new_data = cv.transform(new_data).toarray()
    prediction = model.predict(new_data)
    return render_template("index.html", prediction = prediction)

if __name__ == "__main__":
    app.run(debug = True)