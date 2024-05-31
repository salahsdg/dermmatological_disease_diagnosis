import os
import uuid
from PIL import Image
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import load_img, img_to_array

ALLOWED_EXT = {'jpg', 'jpeg', 'png', 'jfif'}
classes = [
    'Actinic Keratoses',
    'Basal Cell Carcinoma',
    'Benign Keratosis',
    'Dermatofibroma',
    'Melanoma',
    'Melanocytic Nevi',
    'Vascular naevus'
]

# Load model
with open('predictions/model.json', 'r') as j_file:
    loaded_json_model = j_file.read()
model = model_from_json(loaded_json_model)
model.load_weights('predictions/model.h5')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

def predict(filename):
    img = load_img(filename, target_size=(224, 224))
    img = img_to_array(img)
    img = img.reshape(1, 224, 224, 3)
    img = img.astype('float32')
    img = img / 255.0
    result = model.predict(img)
    
    dict_result = {result[0][i]: classes[i] for i in range(7)}

    res = sorted(result[0], reverse=True)
    prob = res[:3]

    prob_result = [(prob[i] * 100).round(2) for i in range(3)]
    class_result = [dict_result[prob[i]] for i in range(3)]
    
    return class_result, prob_result
