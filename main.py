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


user_api = "feb016b366921fdd8121b7b5c120839a"
st.sidebar.subheader("Find your city weather here")
city = st.sidebar.text_input(label="Enter a city Name")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
hmdt = api_data['main']['humidity']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

st.sidebar.write("Weather Stats for - {}  || {}".format(city.upper(), date_time))
st.sidebar.write("Current temperature is: {:.2f} °C".format(temp_city))
st.sidebar.write("Current Humidity      :",hmdt, '%')

