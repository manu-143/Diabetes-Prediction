from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/predict_diabities', methods = ['GET','POST'])
def predict_diabities():
    Pregnancies = float(request.form['Pregnancies'])
    Glucose=float(request.form['Glucose'])
    BloodPressure=float(request.form['BloodPressure'])
    SkinThickness=float(request.form['SkinThickness'])
    Insulin=float(request.form['Insulin'])
    BMI=float(request.form['BMI'])
    DiabetesPedigreeFunction=float(request.form['DiabetesPedigreeFunction'])
    Age=int(request.form['Age'])

    response = jsonify({
        'estimation':util.get_estimation(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Diabities Price Prediction...")
    util.load_saved_artifacts()
    app.run()
