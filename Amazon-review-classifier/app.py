import numpy as numpy
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model_knn.pkl', 'rb'))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    new_data = cv.transform(int_features).toarray()
    prediction = model.predict(new_data)
    print(prediction)
    return "This was your inputted string {}".format(int_features) 

if __name__ == "__main__":
    app.run(debug = True)

