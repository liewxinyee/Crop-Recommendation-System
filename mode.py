from PIL import Image
from models import testing
from selectbox import SelectCrop
import crops
import streamlit as st


def envFac():
    st.title('Crop Recommendation System 🌱')
    image = Image.open('background.jpg')
    st.image(image, use_column_width=True)
    st.markdown("""
    ### This app recommends the most suitable crop for you!👨‍🌾 \nInstructions: Key in the following values and click the 'Predict' button
    """)
    testing()

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
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">Source code: !!</p>', unsafe_allow_html=True)



