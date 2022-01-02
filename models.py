import pickle
import streamlit as st
import numpy as np
import os
import base64
from PIL import Image

def load_model(modelfile):
    loaded_model = pickle.load(open(modelfile, 'rb'))
    return loaded_model



CROP_IMG_PATH = 'Crops_images'
crop_img_files = [os.path.join(CROP_IMG_PATH, f) for f in os.listdir(CROP_IMG_PATH)]

def get_img_file(pred, crops_list=crop_img_files):
    crop_name = pred[0]
    img_file = [f for f in crops_list if crop_name in f][0]
    return img_file


def get_image(img_path):
    encoded_image = base64.b64encode(open(img_path, 'rb').read())
    img_src = 'data:image/png;base64,{}'.format(encoded_image.decode())
    return img_src

def predict(filename):
    N = st.number_input("Nitrogen")
    P = st.number_input("Phosporus")
    K = st.number_input("Potassium")
    temp = st.number_input("Temperature in °C")
    humidity = st.number_input("Humidity in %")
    ph = st.number_input("pH")
    rainfall = st.number_input("Rainfall in mm")

    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    if st.button('Predict'):
        loaded_model = load_model(filename)
        prediction = loaded_model.predict(single_pred)
        pred_img_file = get_img_file(prediction)
        fig = get_image(pred_img_file)
        st.write('''
                 ## Results 🔍 
                 ''')
        col1, col2 = st.columns([2, 2])

        with col1:
            st.image(fig,  use_column_width=True)

        with col2:
            st.success(f"{prediction.item().title()} is recommended for your farm.")

def DT():
    st.subheader("Decision Tree")
    predict('DT.pkl')

def NB():
    st.subheader("Naive Bayes")
    predict('NB.pkl')

def SVM():
    st.subheader("Support Vector Machine(SVM)")
    predict('SVM.pkl')

def LR():
    st.subheader("Logistic Regression")
    predict('LR.pkl')

def RF():
    st.subheader("Random Forest")
    predict('RF.pkl')

def XB():
    st.subheader("XGBoost")
    predict('XGB.pkl')







