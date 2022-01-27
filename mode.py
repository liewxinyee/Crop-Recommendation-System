from PIL import Image
from models import recommend
from selectbox import SelectCrop
import crops
import streamlit as st
import pandas as pd

def home():
    st.title('Crop Recommendation System ')
    st.markdown("""
            ### This app recommends the most suitable crop for you!👨‍🌾 
            """)
    df = pd.read_csv(r'CropRecommendation_Cleaned.csv')
    with st.expander("Click to See The Dataset Overview"):
        col1, col2, col3 = st.columns([6, 1, 2])
        with col1:
            st.dataframe(df)
        with col2:
            st.write()
        with col3:
            st.metric(label="Total Crop Type", value = 11)
    image = Image.open('background.jpg')
    st.image(image, use_column_width=True)


def envFac():
    st.markdown("""
            ### Instructions: Key in the following values and click the 'Predict' button
            """)
    recommend()

def graphs():
    nitrogen = Image.open('nitrogen.jpg')
    phosphorus = Image.open('phosphorus.jpg')
    potassium = Image.open('potassium.jpg')
    weather = Image.open('weather.jpg')
    with st.expander("Click to See The Comparison for Each Crop"):
        type = st.radio("Select A Factor",
                        ('Nitrogen(N)','Phosphorus(P)','Potassium(K)','Weather Factors'))
        if type == 'Nitrogen(N)':
            st.image(nitrogen,use_column_width=True)
        elif type == 'Phosphorus(P)':
            st.image(phosphorus, use_column_width=True)
        elif type == 'Potassium(K)':
            st.image(potassium, use_column_width=True)
        elif type == 'Weather Factors':
            st.image(weather, use_column_width=True)


def selectCrop():
    crop = SelectCrop()
    crop.add_app("Apple", crops.apple)
    crop.add_app("Banana", crops.banana)
    crop.add_app("Blackgram", crops.blackgram)
    crop.add_app("Chickpea", crops.chickpea)
    crop.add_app("Coconut", crops.coconut)
    crop.add_app("Coffee", crops.coffee)
    crop.add_app("Cotton", crops.cotton)
    crop.add_app("Grapes", crops.grapes)
    crop.add_app("Jute", crops.jute)
    crop.add_app("Kidneybeans", crops.kidneybeans)
    crop.add_app("Lentil", crops.lentil)
    crop.add_app("Maize", crops.maize)
    crop.add_app("Mango", crops.mango)
    crop.add_app("Mothbeans", crops.mothbeans)
    crop.add_app("Mungbean", crops.mungbean)
    crop.add_app("Muskmelon", crops.muskmelon)
    crop.add_app("Orange", crops.orange)
    crop.add_app("Papaya", crops.papaya)
    crop.add_app("Pigeonpeas", crops.pigeonpeas)
    crop.add_app("Pomegranate", crops.pomegranate)
    crop.add_app("Rice", crops.rice)
    crop.add_app("Watermelon", crops.watermelon)
    crop.run()



def about():
    st.header("Crop Recommendation System🌱")
    st.subheader("About This Application🍃")
    st.write("This app takes environmental factors including temperature, humidity, rainfall and soil parameters which are the amount of nitrate, phosphorus, calcium and pH value of the soil into consideration to recommend the most suitable crop to the users.")
    st.write("It aims to recommend the most suitable crop according to the given soil factors and climate conditions to the users")
    st.subheader("Documentation📄")
    st.write("Detailed documentation can be found at https://drive.google.com/file/d/1RfzBFZkyqVqN_hs2DvKbla4mD420-ZoB/view?usp=sharing")
    st.subheader("Dataset Information📊")
    st.write("The dataset used is obtained from Kaggle https://www.kaggle.com/atharvaingle/crop-recommendation-dataset")
    st.subheader("Source Code👇")
    st.write("Complete source code can be accessed at https://github.com/liewxinyee/Crop-Recommendation-System")
    st.subheader("About Author🙎")
    st.write("Hello! I am Liew Xin Yee from Malaysia, currently a thrid year Data Science student from University of Malaya.")
    st.write("If you have any inquiries or feedback about this project, feel free to contact me via my email xiinyeeliew@gmail.com✉️")
    st.markdown("""
      ######  &nbsp [![this is an image link](https://camo.githubusercontent.com/d7b9f7e3f8af9348678c5042440844da48b892fb320482f313d28366d10c25d5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c696e6b6564496e2d2532333030373742352e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d6c696e6b6564696e266c6f676f436f6c6f723d7768697465)](https://www.linkedin.com/in/liew-xin-yee-65a534214/)
      """, unsafe_allow_html=True)
