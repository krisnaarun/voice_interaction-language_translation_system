import streamlit as st
from streamlit_option_menu import option_menu
import Home, Image, Video, Voice

st.set_page_config(
    page_title='Voice Interaction & Translation',
    page_icon='✌️',
)

# st.title('AI-DRIVEN LANGUAGE TRANSLATION & VOICE INTERACTION SYSTEM')
# st.sidebar.success('select a page above ☝️')

class MultiApp:
    def __init__(self):
        self.apps=[]
    def add_app(self,title,function):
        self.apps.append({
            'title':title,
            'function':function
        })
    def run():
        with st.sidebar:
            app=option_menu(
                menu_title='Choose One',
                options=['Home','Image Text Translation','Video Voice Translation','Voice Interaction System'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    'container':{'padding': '5!important','background-color':'red'},
                    'nav-link':{'color':'white','font-size':'15px','text-align':'left'},
                    'nav-link-selected':{'background-color':'black'}
                     }
            )
        if app=='Home':    
            Home.app()
        if app=='Image Text Translation':    
            Image.app()
        if app=='Video Voice Translation':    
            Video.app()
        if app=='Voice Interaction System':    
            Voice.app()
    run()

            