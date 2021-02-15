from flask import Flask,request, url_for, redirect, render_template
import numpy as np
from tensorflow.keras.models import load_model
import cv2
import os

app = Flask(__name__)

model = load_model("model/plant_resnet_model.h5")

input_shape = model.input_shape
classes = ['healthy', 'multiple_diseases', 'rust', 'scab']

@app.route('/')
def hello_world():
    return render_template("plant_pathology.html")

app.config["IMAGE_UPLOADS"] = "images"

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == "POST":
        if request.files:
            img = request.files['img']
            path = os.path.join(app.config["IMAGE_UPLOADS"], img.filename)
            img.save(path)
            print("image saved !")
            
            img = cv2.imread(path)
            img = cv2.resize(img, (input_shape[2], input_shape[1]))

            img_array = np.ndarray(shape=(1, input_shape[1], input_shape[2], 3), dtype=int)
            img_array[0] = img

            pred = model.predict(img_array)
            pred_class = np.argmax(pred[0])
            pred_class = classes[pred_class]
            
            #return render_template('plant_pathology.html', pred="Predicted class: {}".format(pred_class), img="<img src='{}' alt='plant image' title='plant image' height=200 align='center' />".format(path))
            return render_template('templates/plant_pathology.html', pred="Predicted class: {}".format(pred_class), user_image=path)
            
    return render_template('templates/plant_pathology.html', pred="Please try again !")


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=8080)
