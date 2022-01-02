import streamlit as st
from PIL import Image
import requests
from datetime import datetime

st.set_page_config(page_title="Crop Recommendation System",
                   layout = "wide")

st.title('Crop Recommendation System 🌱')
#image = Image.open('background.jpg')
#st.image(image, use_column_width=True)
st.markdown("""
### This app recommends the most suitable crop for you! \n Find out the most suitable crop to grow in your farm 👨‍🌾
""")


from selectbox import SelectMode
import mode
import json

home = SelectMode()
home.add_app("Input Environmental Factors", mode.envFac)
home.add_app("Select a Crop", mode.selectCrop)

home.run()

