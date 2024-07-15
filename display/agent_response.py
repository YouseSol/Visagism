import streamlit as st

def display_agents_response(responses : list = []):
    if len(responses) == 0: return 

    images = [
        "Visagist.jpg",
        "Analist.jpg",
        "Cut_analist.jpg"
    ]

    names = [
        "Especialista em Análise Corporal",
        "Especialista em Análise Visagista",
        "Especialista em Barbearia Visagista"
    ]

    for i in range(len(images)):
        with st.container(border=True):
            st.image(f"assets/{images[i]}")
            st.markdown(f"### {names[i]}")
            st.divider()
            st.write(responses[i])