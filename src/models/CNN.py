from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array
import numpy as np
import os
import PIL

__model = None
def load_model_cnn():
    global __model
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_file = os.path.join(base_dir, '..', '..', 'models', 'CNN_model.keras')
    __model = load_model(model_file)

def predict_model(image_path):
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")

        test_img = PIL.Image.open(image_path)
        test_img = test_img.convert("RGB")
        test_img = test_img.resize((256, 256))

        test_img_array = img_to_array(test_img)
        test_img_array = np.expand_dims(test_img_array, axis=0)
        test_img_array = test_img_array / 255.0

        # Predict with the model
        prediction = __model.predict(test_img_array)
        result = "Pneumonia" if prediction >= 0.5 else "Normal"
        return result

    except Exception as e:
        print(f"Error during prediction: {e}")
        return None

if __name__ == '__main__':
    # Define paths
    image_path = r'C:/Users/Asghar Qambar Rizvi/OneDrive/Desktop/pne.jpeg'

    # Load model and make prediction
    load_model_cnn()
    if __model:
        predict_model(image_path)