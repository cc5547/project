import streamlit as st
import UI as ui
import base64
from pydub.playback import play
from Functional import GetResult  

def set_BGM():
    try:
        audio_path = "DL_Project/Data_csv/outdoor_crackling_fire_sound.mp3"
        audio_file = open(audio_path, 'rb').read()

        st.markdown(f'<audio autoplay loop="true" src="data:audio/mp3;base64,\
                    {base64.b64encode(audio_file).decode()}"></audio>',\
                    unsafe_allow_html = True)          
    except Exception as e : 
            return st.error(e)

def main() : 
    ui.set_page()
    set_BGM()

    get = GetResult()

    df, area, direction = get.choice_result()

    if df is not None : 
        ui.set_background()

        with st.sidebar : 
            ui.sidebar_print_df(df)
        
        if direction == "전체" or direction == "가평군" or direction == "포천시" :
            ui.title_ment(area, direction, len(df))
            ui.cutting()
            get.get_price()

        else : ui.refactoring_ment()
    else : ui.start_background()

if __name__ == '__main__' : 
    main()