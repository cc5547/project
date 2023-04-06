import streamlit as st
from ChoiceArea import GetSideBar
st.set_page_config(page_title="DL", layout="wide")

def user_interface():
    st.title("뼈대 작업 중...")

    # 사이드바 연동 성공 여부 
    st.subheader(True) if GetSideBar().result_sidebar() is None else st.subheader(False)

    image = ["https://i.imgur.com/t4O7ozH.jpg", "https://i.imgur.com/idnsDBs.gif", "https://i.imgur.com/fvRG1Tj.gif"]
    
    with st.expander("Panel title"):
        st.image(image[0], width = 700)

    containers = [st.container() for i in range(len(image))]
    
    for i in range(len(image)) :
        with containers[i] : 
            st.image(image[i], width = 700)
    st.expander("asd")