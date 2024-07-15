import streamlit as st
from Agency.CutAgency import cut_agency
from display.agent_response import display_agents_response

from PIL import Image
import io

def visagism_page():

    st.image("assets/visagism_banner.png")
    
    st.markdown("##")

    with st.container(border=True):
        st.markdown("## Carregue as fotos do cliente aqui 👇")

        st.divider()

        c1, c2 = st.columns(2, gap="large")

        with c1:
            frontal_image = st.file_uploader(label="Carregue o rosto frontal aqui!")
            
        with c2:
            lateral_image = st.file_uploader(label="Carregue o rosto lateral aqui!")

        st.divider()

        submit_btn = st.button("Gerar o relatório automaticamente!")


    if submit_btn:

        # st.image("assets/Analist.jpg")
        # st.markdown("## Teste")
        
        if 'frontal_photo' not in st.session_state:
            st.session_state['frontal_photo'] = frontal_image 
        if 'lateral_photo' not in st.session_state:
                st.session_state['lateral_photo'] = lateral_image 
        
        if frontal_image is not None:
            file_name = frontal_image.name
            frontal_image = frontal_image.read()

            image = Image.open(io.BytesIO(frontal_image))

            with st.spinner('A Agência de Visagismo está trabalhando...'):
                # visagist_response, analist_response, cut_analist_response = cut_agency(image)
                responses = cut_agency(image)

            display_agents_response(responses)
                    