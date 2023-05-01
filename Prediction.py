import io
import base64
import os
import tensorflow as tf
from PIL import Image
import numpy as np
import keras.utils as i


categories_parts = ["Elbow", "Finger", "Forearm", "Humerus", "Hand", "Shoulder", "Wrist"]

#   0-fractured     1-normal
categories_fracture = ['fractured', 'normal']




class Prediction():
    result = ""
    image = ""
    choice = 0
    model_parts = tf.keras.models.load_model("../ObjectDtectionModel/weights/ResNet50_BodyParts.h5")
    model_elbow_frac = tf.keras.models.load_model("../ObjectDtectionModel/weights/ResNet50_Elbow_frac.h5")
    model_hand_frac = tf.keras.models.load_model("../ObjectDtectionModel/weights/ResNet50_Hand_frac.h5")
    model_shoulder_frac = tf.keras.models.load_model("../ObjectDtectionModel/weights/ResNet50_Shoulder_frac.h5")
    model_humerus_frac = tf.keras.models.load_model("../ObjectDtectionModel/weights/ResNet50_Humerus_frac.h5")
    model_finger_frac = tf.keras.models.load_model("../ObjectDtectionModel/weights/ResNet50_Finger_frac.h5")
    model_forearm_frac = tf.keras.models.load_model("../ObjectDtectionModel/weights/ResNet50_Forearm_frac.h5")
    model_wrist_frac = tf.keras.models.load_model("../ObjectDtectionModel/weights/ResNet50_Wrist_frac.h5")



def loadModels():
    print("wwwwwwwwwwwwwwwwwwwwwwwww")
    Prediction.model_parts = tf.keras.models.load_model("weights/ResNet50_BodyParts.h5")
    Prediction.model_elbow_frac = tf.keras.models.load_model("weights/ResNet50_Elbow_frac.h5")
    Prediction.model_hand_frac = tf.keras.models.load_model("weights/ResNet50_Hand_frac.h5")
    Prediction.model_shoulder_frac = tf.keras.models.load_model("weights/ResNet50_Shoulder_frac.h5")
    Prediction.model_humerus_frac = tf.keras.models.load_model("weights/ResNet50_Humerus_frac.h5")
    Prediction.model_finger_frac = tf.keras.models.load_model("weights/ResNet50_Finger_frac.h5")
    Prediction.model_forearm_frac = tf.keras.models.load_model("weights/ResNet50_Forearm_frac.h5")
    Prediction.model_wrist_frac = tf.keras.models.load_model("weights/ResNet50_Wrist_frac.h5")

def predict(img, model="Parts"):
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    size = 224
    if model == 'Parts':
        chosen_model = Prediction.model_parts
    else:
        if model == 'Elbow':
            chosen_model = Prediction.model_elbow_frac
        elif model == 'Hand':
            chosen_model = Prediction.model_hand_frac
        elif model == 'Shoulder':
            chosen_model = Prediction.model_shoulder_frac
        elif model == 'Finger':
            chosen_model = Prediction.model_finger_frac
        elif model == 'Forearm':
            chosen_model = Prediction.model_forearm_frac
        elif model == 'Humerus':
            chosen_model = Prediction.model_humerus_frac
        elif model == 'Wrist':
            chosen_model = Prediction.model_wrist_frac
    print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    img_bytes = base64.b64decode(img)

    # Load the bytes into a PIL Image object
    imgs = Image.open(io.BytesIO(img_bytes))


    imgs.save('myimage_500.jpg')
    temp_img = i.load_img('myimage_500.jpg', target_size=(size, size))
    os.remove('myimage_500.jpg')

    print("ccccccccccccccccccccc")
    x = i.img_to_array(temp_img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    print("ddddddddddddddddddddddddddddddddddd")
    prediction = np.argmax(chosen_model.predict(images), axis=1)
    print("ssssssssssssssssssss")
    # chose the category and get the string prediction
    if model == 'Parts':
        prediction_str = categories_parts[prediction.item()]
    else:
        prediction_str = categories_fracture[prediction.item()]
    print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    Prediction.result = prediction_str
    Prediction.choice=0
    return prediction_str