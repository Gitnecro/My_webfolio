import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coder = load_lottieurl("https://lottie.host/d058c313-ca92-4e3c-9f8e-803c97081e17/zURrJMOE6x.json")
img = Image.open('pose.png')

st.write("##")
st.subheader("Hey there hope you are doing well :wave: ")
st.title("Shivam Varshney")
st.write("""

What's meant to be will always find a way .

""")

st.write('---')

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects', 'Contact'],
        icons=['person', 'code-slash', 'chat-left-text-fill'],
        orientation='horizontal'
    )
if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)
    with col1:
        st.write("##")
        st.subheader("I am Shivam Varshney")
        st.title("Undergrad at Vellore institute of technology")
    with col2:
        st_lottie(lottie_coder)

    st.write("---")

    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("""
            Education
            - Vellore institute of technology 
                - Bachelor of Engineering -Electronics and Computer Engineering
                - Grade: 8.02
            - Class XII
                - PCMB
                - Grade: 8.4
            - Class X 
                - Grade: 9.4
            """)
        with col4:
            st.subheader("""
            Experience
            - Committee Member
                - IEEE Computing Society




            """)

if selected == "Projects":
    with st.container():
        st.header("My Projects")
        st.write("##")
        col5, col6 = st.columns((1, 2))

        with col5:
            st.image(img)
        with col6:
            st.subheader("Robust Human Target Detection System")
            st.write("""

            We made this in a team for our hackathon

            """)
            st.markdown("[link to my project](streamlit.io)")