import streamlit as st
import pickle
import pandas as pd

def set_page() : 
    return st.set_page_config(page_title="DL", page_icon=":smiley:", layout="wide")

def set_background():
    return st.markdown("""<style>
                        .main {
                            background-image: url('https://i.imgur.com/PSeW0pm.gif');
                            background-size: cover;
                        }
                        </style> """, unsafe_allow_html=True)


def start_background() : 
    return st.markdown("""<style>
                        .main {
                            background-image: url('https://i.imgur.com/idnsDBs.gif');
                            background-size: cover;
                        }
                        </style> """, unsafe_allow_html=True)

def title_ment(area, direction) : 
    return st.markdown(f"<div style='background-color: green; \
                        padding: 10px; color: white; font-size: 48px;\
                        font-weight: bold; display: inline-block;'> \
                        👉{area} {direction} \
                        </div>", unsafe_allow_html=True)

def cutting() : 
    return st.markdown("---")

def result_chart() : 
    return st.image("https://i.imgur.com/NuieMp3.png", width = 1200)

def gapyung_load():
    # pkl_gapyeong_path = "DL_Project/Data_csv/autogluon_gapyeong.pkl"
    # pkl_pocheon_path = "DL_Project/Data_csv/autogluon_pocheon.pkl"
    # pkl_total_path = "DL_Project/Data_csv/autogluon_total.pkl"

    # with open(pkl_gapyeong_path, 'rb') as gapyeong, \
    #     open(pkl_pocheon_path, 'rb') as pocheon, \
    #     open(pkl_total_path, 'rb') as total:
    #     return pickle.load(gapyeong), pickle.load(pocheon), pickle.load(total)
    gapyung_path = "https://github.com/cc5547/project/blob/main/DL_Project/Data_csv/gapyeong.csv"
    try :  
        return pd.read_csv(gapyung_path)
    except Exception as e : 
        return st.error(e)
    

















# return st.image("https://i.imgur.com/idnsDBs.gif", width = 1200)
# with st.expander(mecanism_ment()) : mechanism_image()
# def search_result(area, direction) : return st.write(f"### 선택한 결과 입니다. ") 

# def mecanism_ment() : return "# 메커니즘_설명 / 용량이 엄청 클 것 으로 예상 되기에 메모리 최적화. "
# def mechanism_image() : return st.image("https://i.imgur.com/SgRVHOk.jpg", width = 1000)

# def image() : return ["https://i.imgur.com/t4O7ozH.jpg", "https://i.imgur.com/idnsDBs.gif", "https://i.imgur.com/fvRG1Tj.gif"]
# def containers() : return [st.container() for i in range(len(image()))]
    # for i in range(len(image())) :
    #         with containers()[i] : st.image(image()[i], width = 700)



    # image = [
    #     "https://i.imgur.com/t4O7ozH.jpg", 
    #     "https://i.imgur.com/idnsDBs.gif", 
    #     "https://i.imgur.com/fvRG1Tj.gif"
    #     ]

    # for i in range(len(image)) :
    #     with st.expander(f"사진_{i+1}"):
    #         st.image(image[i])


    # containers = [st.container() for i in range(len(image))]
    # for i in range(len(image)) :
    #     with containers[i] : 
    #         st.image(image[i], width = 700)
    # # =====================================================================
    # messages = ['success', 'info', 'warning', 'error']

    # for i in range(3):
    #     for message in messages:
    #         getattr(st, message)(f'{message} 메세지')