import streamlit as st
from PIL import Image
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

# 데이터 프레임 생성
def create_df():
  df_URL = "https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EC%8B%9C%ED%97%98%EC%9E%A5%EC%86%8C_%EA%B0%80%EA%B3%B5%EC%B2%98%EB%A6%AC.csv"
  df_URL_g1 = "https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EA%B7%B8%EB%9E%98%ED%94%84_1.csv"
  df_URL_g2 = "https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EA%B7%B8%EB%9E%98%ED%94%84_2.csv"

  df = pd.read_csv(df_URL).iloc[:, 1:]
  df_g1 = pd.read_csv(df_URL_g1)
  df_g2 = pd.read_csv(df_URL_g2)

  df.index += 1

  return df, df_g1, df_g2

# 사이드바
def side_bar(df) :
  s_bar = st.sidebar
  s_bar.title('지역을 선택해주세요.')
  
  area = df['지사명'].drop_duplicates().tolist()
  choice = s_bar.selectbox('지역 선택(재검색시 상세 검색을 지워 주세요)', area, index = 10)

  for i in range(len(area)) : 
    if choice == area[i] : result = df[df['지사명'] == area[i]]
    else : pass

  search = s_bar.text_input('상세 검색 (시, 교명등의 키워드를 입력 :smile:)', value = '')
  result = df[(df['지사명'] == choice) & (df['시험장소'].str.contains(search))]
  result.index = np.arange(1, len(result) + 1)

  return result

# 그래프 생성
def create_graph(df_g1, df_g2):
  fig = go.Figure()

  # 그래프_1
  if df_g1 is not None:
    # 문자열에서 % 기호 제거 및 실수 타입으로 변환
    df_g1.iloc[:, 1:] = df_g1.iloc[:, 1:].apply(lambda x: x.str.rstrip('%')).astype(float)

    # 연도별 색상 지정
    colors = px.colors.qualitative.Set3[:len(df_g1.columns)-1]

    for i, col in enumerate(df_g1.columns[1:]):
        fig.add_trace(go.Bar(x=df_g1['Unnamed: 0'], y=df_g1[col], name=col, marker_color=colors[i]))

    # 레이아웃 설정
    fig.update_layout(
        title='필기시험 합격률',
        xaxis_title='시험 분류',
        yaxis_title='합격률%',
        yaxis=dict(range=[0, 100]),
        plot_bgcolor='#e2f3ea', # 차트 배경색 지정
        width=1000,
        height=700,)

  # 그래프_2
  elif df_g2 is not None:
    df_g2 = df_g2.drop(df_g2.columns[1], axis=1)
    years = df_g2.columns[1:]
    colors = px.colors.qualitative.Set3[:len(years)] # 연도별 색상 리스트 생성
    for i, year in enumerate(years):
        fig.add_trace(go.Bar(x=df_g2['구분'], y=df_g2[year], name=year, marker_color=colors[i]),)

    # 레이아웃 설정
    fig.update_layout(
        title='응시자 및 합격자',
        xaxis_title='시험 분류',
        yaxis_title='인원수',
        plot_bgcolor='#e2f3ea', # 차트 배경색 지정
        width=1000,
        height=700,)
  else : pass

  return fig

# main 시작점
def main() : 
  df, df_g1, df_g2 = create_df()
  
  col1, col2 = st.columns([8, 2])
  with col1 : 
    st.title(":smile: 시험장소를 안내해드립니다 :smile:")
    st.dataframe(side_bar(df), width=1000, height=500)
    st.subheader(":smile: 귀하의 합격을 기원합니다! :smile:")
  with col2 : 
    st.markdown("[![Foo](https://i.imgur.com/SywJPmA.png)](https://map.naver.com/)")

  tab1, tab2 = st.tabs(['필기 년도 별 합격률' , '응시자 및 합격자 수'])
  with tab1 : 
    st.plotly_chart(create_graph(df_g1, None))
  with tab2 : 
    st.plotly_chart(create_graph(None, df_g2))

if __name__ == '__main__':
  main()