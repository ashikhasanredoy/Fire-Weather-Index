import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
from sklearn.preprocessing import StandardScaler

# Initialize Flask app
application = Flask(__name__)
app = application

# Load the trained model and scaler
liner_moder = pickle.load(open('models/linear.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict_datapoint", methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        # Get input values from form
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        data = np.array([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        scaled_data = standard_scaler.transform(data)

        result = liner_moder.predict(scaled_data)[0]  # scalar value

        return render_template("home.html", results=result)


    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)