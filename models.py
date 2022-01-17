import pickle
import streamlit as st
import numpy as np
import os
import base64
import pandas as pd
import hydralit_components as hc
import time

def recommend():
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


    N = st.number_input("Ratio of Nitrogen(N) content in soil")
    P = st.number_input("Ratio of Phosphorus(P) content in soil")
    K = st.number_input("Ratio of Potassium(K) content in soil")
    temp = st.number_input("Temperature in °C")
    humidity = st.number_input("Humidity in %")
    ph = st.number_input("pH value of the soil")
    rainfall = st.number_input("Rainfall in mm")

    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

#data = pd.read_csv(r'C:\Users\xy\Desktop\CropRecommendation_app\CropRecommendation_Cleaned')


    if st.button('Predict'):
        with hc.HyLoader('Predicting',hc.Loaders.standard_loaders,index=[3,0,5]):
            time.sleep(3)
        loaded_model = load_model('RF.pkl')
        prediction = loaded_model.predict_proba(single_pred)
        st.write('''
                ## Results 🔍 
                ''')

        def result(input):
            output = pd.DataFrame(prediction, columns=loaded_model.classes_)
            a = output.apply(lambda s, n: pd.Series(s.nlargest(n).index), axis=1, n=3)
            pred_img_file = get_img_file(a[0])
            fig = get_image(pred_img_file)

            col1, col2 = st.columns([2, 2])
            with col1:
                st.image(fig, use_column_width=True)
            with col2:
                st.success(a[0].values)
                st.write("is recommended for your farm.")

            st.subheader('Looking for Alternatives?')

        def result2(input):
            output = pd.DataFrame(prediction, columns=loaded_model.classes_)
            a = output.apply(lambda s, n: pd.Series(s.nlargest(n).index), axis=1, n=3)

            pred_img_file1 = get_img_file(a[1])
            fig1 = get_image(pred_img_file1)
            pred_img_file2 = get_img_file(a[2])
            fig2 = get_image(pred_img_file2)

            col1, col2,col3, col4 = st.columns([2, 2, 2, 2])
            with col1:
                st.image(fig1, use_column_width=True)
            with col2:
                st.write("Second Option:")
                st.success(a[1].values)
            with col3:
                st.image(fig2, use_column_width=True)
            with col4:
                st.write("Third Option:")
                st.success(a[2].values)

        result(single_pred)
        result2(single_pred)







