import json
import pickle
import numpy as np


def predict_diabities(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    
    X= np.zeros(len(x.columns))
    X[0]= Pregnancies
    X[1]= Glucose
    X[2]= BloodPressure
    X[3]= SkinThickness
    X[4]=Insulin
    X[5]=BMI
    X[6]=DiabetesPedigreeFunction
    X[7]=Age
    
    return round(__model.predict([X]) [0],2)

def load_saved_artifacts():
    print("loading saved artifacts.....start")
    global __data_columns

    with open ("C:\Users\lenovo\Desktop\diabities_prediction\server\\artifacts\\columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    with open("server\\artifacts\\Diabities_data.pickle",'rb') as f:
        __model = pickle.load(f)
        print("loading saved artifacts.....done")


if __name__ == '__main__':
    load_saved_artifacts()

    predict_diabities(4, 154,72,29,126,31.3,0.338,37)
    predict_diabities(0,5,50,30,89,30,450,45)