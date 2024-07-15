import streamlit as st
import toml 

from navigation.pages import sideBar
from style.Style import Style
from functions.ThemeChanger import ThemeChanger

st.set_page_config(
    page_title="Visagismo", 
    page_icon="📣",
    layout="wide")

Style()

# theme_changer = ThemeChanger()
# theme_changer.create_button()

st.sidebar.image("assets/BUSINESS_LOGOTYPE.png", caption="Youse Smart Solutions")

sideBar()

