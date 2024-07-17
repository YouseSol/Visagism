from Agents.VisagismEspecialist import VisagismEspecialist
from Agents.Analist import Analist
from Agents.CutAnalist import CutAnalist
import streamlit as st
from dotenv import dotenv_values

def cut_agency(image):
    # api_key = dotenv_values(".env").get("GEMINI_API_KEY")
    api_key = st.secrets["google_api_key"]

    visagist = VisagismEspecialist(api_key=api_key)
    analist = Analist(api_key=api_key)
    cut_analist = CutAnalist(api_key=api_key)

    visagist_response = visagist.request(image=image)
    analist_response = analist.request(document=visagist_response)
    cut_analist_response = cut_analist.request(document=analist_response)

    return visagist_response, analist_response, cut_analist_response
