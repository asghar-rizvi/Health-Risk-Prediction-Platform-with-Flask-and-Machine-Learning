import pickle
import pandas as pd
import os
__model = None


def load_data():
    global __model
    # with open('../../models/kidney.pickle','rb') as f:
    #     __model = pickle.load(f)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pickle_file = os.path.join(base_dir,'..', '..','models','liver.pickle')
    with open(pickle_file, 'rb') as f:
        __model = pickle.load(f)

def predict_liver(Age, Gender, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio):
    features = pd.DataFrame(
        {
            'Age': [Age],
            'Gender': [Gender],
            'Alamine_Aminotransferase': [Alamine_Aminotransferase],
            'Aspartate_Aminotransferase': [Aspartate_Aminotransferase],
            'Total_Protiens': [Total_Protiens],
            'Albumin': [Albumin],
            'Albumin_and_Globulin_Ratio': [Albumin_and_Globulin_Ratio]
        }
    )
    prediction = __model.predict(features)
    return prediction


if __name__ == '__main__' :
    load_data()
    print(predict_liver(
        Age=45,
        Gender=1,  # Assuming 1 for Male and 0 for Female
        Alamine_Aminotransferase=35,
        Aspartate_Aminotransferase=40,
        Total_Protiens=6.8,
        Albumin=3.5,
        Albumin_and_Globulin_Ratio=1.2
    ))
