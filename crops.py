import streamlit as st
import pandas as pd
from PIL import Image

data = pd.read_csv(r'C:\Users\xy\Desktop\CropRecommendation_app\crop_summary.csv')


def summary(string1,int,string2):
    st.subheader("The average value of each environmental factor for " +string1)

    col1, col2, col3= st.columns([2, 2,2])
    with col1:
        for i in ["Potassium(K)","Nitrogen(N)","Phosphorus(P)","Humidity in %","pH","Rainfall in mm","Temperature in °C"]:
            st.write(i,)
    with col2:
        for j in range(len(data)):
            st.write(data.iloc[j, int])
    with col3:
        image = Image.open(string2)
        st.image(image, use_column_width=True)

def apple():
    summary("APPLE", 1,'Crops_images/apple.jpg')

def banana():
    summary("BANANA", 2, 'Crops_images/banana.jpg')

def blackgram():
    summary("BLACKGRAM", 3, 'Crops_images/blackgram.jpg')

def chickpea():
    summary("CHICKPEA", 4, 'Crops_images/chickpea.jpg')

def coconut():
    summary("COCONUT", 5, 'Crops_images/coconut.jpg')

def coffee():
    summary("COFFEE", 6, 'Crops_images/coffee.jpeg')

def cotton():
    summary("COTTON", 7, 'Crops_images/cotton.jpg')

def grapes():
    summary("GRAPES", 8, 'Crops_images/grapes.jpg')

def jute():
    summary("JUTE", 9, 'Crops_images/jute.jpg')

def kidneybeans():
    summary("KIDNEYBEANS", 10, 'Crops_images/kidneybeans.jpg')

def lentil():
    summary("LENTIL", 11, 'Crops_images/lentil.jpg')

def maize():
    summary("MAIZE", 12, 'Crops_images/maize.jpeg')

def mango():
    summary("MANGO", 13, 'Crops_images/mango.jpg')

def mothbeans():
    summary("MOTHBEANS", 14, 'Crops_images/mothbeans.jpg')

def mungbean():
    summary("MUNGBEAN", 15, 'Crops_images/mungbean.jpg')

def muskmelon():
    summary("MUSKMELON", 16, 'Crops_images/muskmelon.jpg')

def orange():
    summary("ORANGE", 17, 'Crops_images/orange.jpg')

def papaya():
    summary("PAPAYA", 18, 'Crops_images/papaya.jpg')

def pigeonpeas():
    summary("PIGEONPEAS", 19, 'Crops_images/pigeonpeas.jpg')

def pomegranate():
    summary("POMEGRANATE", 20, 'Crops_images/pomegranate.jpg')

def rice():
    summary("RICE", 21, 'Crops_images/rice.jpg')

def watermelon():
    summary("WATERMELON", 22, 'Crops_images/watermelon.jpg')




