import streamlit as st
import UI as ui
# import base64
from pydub.playback import play
from Functional import GetResult

# def audio_BGM():
#     audio_file = open('DL_Project/Data_csv/outdoor_crackling_fire_sound.mp3', 'rb').read()
#     return st.markdown(f'<audio autoplay loop="true" src="data:audio/mp3;base64,\
#                         {base64.b64encode(audio_file).decode()}"></audio>',\
#                         unsafe_allow_html=True)

def get_search_result() : 
    return GetResult().get_result()

def sidebar_print_df(df) : 
    return st.dataframe(df, width=600)

def main() : 
    ui.set_page()

    ui.audio_BGM()

    df, area, direction = get_search_result()

    if df is not None : 
        ui.set_background()
        ui.title_ment(area, direction)
        ui.cutting()

        with st.sidebar : 
            sidebar_print_df(df)

        ui.result_chart()
    
        # containers = [st.container() for i in range(len(df['업체명']))]
        # for i in range(len(df['업체명'])) :
        #     with containers[i]:
        #         st.write(df.loc[i, 1])

    else : 
        ui.start_background()

if __name__ == '__main__' : 
    main()