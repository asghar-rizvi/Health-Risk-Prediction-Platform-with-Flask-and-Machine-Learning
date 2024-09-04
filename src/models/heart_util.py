import pickle
import pandas as pd
import os
__model = None


def load_data():
    global __model
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pickle_file = os.path.join(base_dir,'..', '..','models','heart.pickle')
    with open(pickle_file, 'rb') as f:
        __model = pickle.load(f)

def predict_heart(age, sex, cp, trestbps, chol, fbs, restecg, thalach,slope,ca,thal):
    features = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }])

    prediction = __model.predict(features)
    return prediction

if __name__ == '__main__' :
    load_data()
    prediction = predict_heart(age=45, sex=1, cp=2, trestbps=130, chol=250, fbs=0, restecg=1, thalach=150, slope=2,
                               ca=0, thal=1)
    print(prediction)
