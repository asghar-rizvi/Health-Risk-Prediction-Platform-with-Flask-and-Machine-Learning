import pickle
import json
import numpy as np
import pandas  as pd
import os

__model = None
__list = None

def load_data():
    global __model
    global __list

    base_dir = os.path.dirname(os.path.abspath(__file__))
    pickle_file = os.path.join(base_dir,'..', '..','models','diabetes.model.pickle')
    with open(pickle_file, 'rb') as f:
        __model = pickle.load(f)

    json_file = os.path.join(base_dir,'..', 'features', 'diabetes.json')
    with open(json_file,'r') as f:
        __list = json.load(f)



def predict_diabetes(gender, age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level, smoking_history):
    df = np.zeros(len(__list))
    df[0] = gender
    df[1] = age
    df[2] = hypertension
    df[3] = heart_disease
    df[4] = bmi
    df[5] = HbA1c_level
    df[6] = blood_glucose_level
    try:
        index = __list.index(smoking_history)
        df[index] = 1
    except ValueError:
        df[7] = 0
    df = pd.DataFrame([df], columns=__list)
    return __model.predict(df)

if __name__ == '__main__' :
    load_data()
    print(predict_diabetes(45, 1, 1, 0, 24.5, 5.8, 150, 'former smoker'))
