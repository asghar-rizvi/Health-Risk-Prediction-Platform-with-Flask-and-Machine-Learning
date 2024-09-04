import pickle
import pandas as pd
import os
__model = None


def load_data():
    global __model
    # with open('../../models/kidney.pickle','rb') as f:
    #     __model = pickle.load(f)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pickle_file = os.path.join(base_dir,'..', '..','models','kidney.pickle')
    with open(pickle_file, 'rb') as f:
        __model = pickle.load(f)

def predict_kidney_disease(age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane):
    features = pd.DataFrame([{
        "age": age, "bp": bp, "sg": sg, "al": al, "su": su, "rbc": rbc, "pc": pc,
        "pcc": pcc, "ba": ba, "bgr": bgr, "bu": bu, "sc": sc, "sod": sod, "pot": pot,
        "hemo": hemo, "pcv": pcv, "wc": wc, "rc": rc, "htn": htn, "dm": dm, "cad": cad,
        "appet": appet, "pe": pe, "ane": ane
    }])

    prediction = __model.predict(features)
    return prediction

if __name__ == '__main__' :
    load_data()
    sample_values = {
        "age": 45.0,
        "bp": 80.0,
        "sg": 1.020,
        "al": 1.0,
        "su": 0.0,
        "rbc": 1,  # Normal
        "pc": 0,  # Abnormal
        "pcc": 1,  # Present
        "ba": 0,  # Not Present
        "bgr": 120.0,
        "bu": 30.0,
        "sc": 1.1,
        "sod": 140.0,
        "pot": 4.0,
        "hemo": 13.0,
        "pcv": 40.0,
        "wc": 6000.0,
        "rc": 5.0,
        "htn": 1,  # Yes
        "dm": 0,  # No
        "cad": 1,  # Yes
        "appet": 1,  # Good
        "pe": 0,  # No
        "ane": 1  # Yes
    }
    prediction = predict_kidney_disease(
        sample_values["age"],
        sample_values["bp"],
        sample_values["sg"],
        sample_values["al"],
        sample_values["su"],
        sample_values["rbc"],
        sample_values["pc"],
        sample_values["pcc"],
        sample_values["ba"],
        sample_values["bgr"],
        sample_values["bu"],
        sample_values["sc"],
        sample_values["sod"],
        sample_values["pot"],
        sample_values["hemo"],
        sample_values["pcv"],
        sample_values["wc"],
        sample_values["rc"],
        sample_values["htn"],
        sample_values["dm"],
        sample_values["cad"],
        sample_values["appet"],
        sample_values["pe"],
        sample_values["ane"],
    )

    print(prediction)