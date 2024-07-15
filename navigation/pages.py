import streamlit as st
from streamlit_option_menu import option_menu

from page_functions.visagism import visagism_page

def sideBar():
    with st.sidebar:
        selected = option_menu(menu_title="", 
                               options=["Análise Automática"],
                               icons=["camera"],
                               menu_icon="cast",
                               default_index=0)
        
    if selected == "Análise Automática":
        visagism_page()