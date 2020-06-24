# load_model_sample.py
from tensorflow.keras.models import load_model
from keras.preprocessing import image
# import matplotlib.pyplot as plt
import numpy as np
import os
import cv2
from PIL import Image



def load_image(img_path, show=False):


    img = Image.open(img_path)
    # img = np.array(img)
    img = img.resize((256,256))
    # img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

    # img = np.fromstring(img_path.read(), np.uint8)
    # img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    # img = cv2.resize(img,(256,256))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)

    return img_tensor
    
def class_name(pred):
    pred = np.argmax(pred, axis=1)
    target_names = {'Bacterial Spot': 0,
                    'Black Measles': 1,
                    'Black Rot': 2,
                    'Blight': 3,
                    'Healthy': 4,
                    'Mold': 5}
    pred = [k for k, v in target_names.items() if v == pred[0]]
    return pred
