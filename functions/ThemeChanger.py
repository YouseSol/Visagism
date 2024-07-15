import streamlit as st
import toml

class ThemeChanger:
    def __init__(self, 
                 config_path : str = ".streamlit/config.toml") -> None:
        self.config_path = config_path

        with open(self.config_path, 'r') as f:
            self.config = toml.load(f)

        self.themes_mode = {
            "light": {
                "base":"light",
                "primaryColor":"black"
            },
            "dark": {
                "base": "dark",
                "primaryColor":"red"
            }
        }

        if "current_theme" not in st.session_state:
            st.session_state['current_theme'] = 'light'
            self.change_theme()

        
    def change_theme(self):
        if st.session_state['current_theme'] == 'light':
            mode = 'dark'
        else:
            mode = 'light'

        new_theme = self.themes_mode[mode]
        self.config['theme']['base'] = new_theme['base']
        self.config['theme']['primaryColor'] = new_theme['primaryColor']

        f = open(self.config_path, 'w')
        toml.dump(self.config, f)
        f.close()

        st.rerun()


    def create_button(self):
        btn_icon = "🌜" if st.session_state['current_theme'] == 'light' else "🌞"
        face_btn = st.button(btn_icon, on_click=self.change_theme)
