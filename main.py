import streamlit as st
import hydralit_components as hc
import mode
from PIL import Image

st.set_page_config(page_title="Crop Recommendation System",layout='wide',initial_sidebar_state='collapsed',)
st.title('Crop Recommendation System 🌱')
image = Image.open('background.jpg')
st.image(image, use_column_width=True)
st.markdown("""
### This app recommends the most suitable crop for you!👨‍🌾 \n Instructions: Key in the following values and click the 'Predict' button
""")


# specify the primary menu definition
menu_data = [
    {'icon': "far fa-copy", 'label':"Overview"},
    {'icon': "fas fa-info-circle", 'label':"About"},
]

over_theme = {'txc_inactive': '#FFFFFF','menu_background':'#62BD69'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)

if (f"{menu_id}") == "Home":
    mode.envFac()
elif (f"{menu_id}") == "Overview":
    mode.selectCrop()
    mode.graphs()
elif (f"{menu_id}") == "About":
    mode.about()
