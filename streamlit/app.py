from matplotlib import colors as mcolors  ## 첫번째 프로토타입
import matplotlib.pyplot as plt           ## 그래프, 동영상 업로딩 용이 
                                          ## 
from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d import Axes3D
# import comedata1 as cd1
import altair as alt
import streamlit as st         
import numpy as np
import pandas as pd
import comedata as cd


MFL_df = cd.MFLdf
AREA_df = cd.AREAdf
MFL_df1 = MFL_df.drop('id', axis=1)
AREA_df1 = AREA_df.drop('id', axis=1)


def main():
    st.title("PROJECT")
    st.write("\n")
    st.write("센서데이터 활용 건설안전을 위한 신호분석 및 모델링 프로젝트입니다")
    st.write("\t\a멘토 -신주호")
    st.write("\n")
    st.write("\t\a조원 - 김용준,배형근,변영준")
    st.write("\n")
    st.write("\t\a프로젝트 기간 - 2021년 3월 8일 ~ 2021년 5월 18일")
    st.image('C:\\Users\\kyjoo\\Desktop\\산학자료\\code\\streamlit\\cone.jpg')


def MFL():
    st.title("MFL Data")
    st.write("\n")
    sensor_list = MFL_df1.columns.unique()
    sensors = st.multiselect(
        "센서 선택", list(sensor_list)), [
            sensor_list[0], sensor_list[1]]

    st.line_chart(MFL_df1)
    if st.checkbox('Show dataframe'):
        st.dataframe(MFL_df1)
    st.image("C:\\Users\\kyjoo\\Desktop\\산학자료\\image\\\m1.jpg")


def AREA():
    st.title("AREA Data")
    st.write("\n")

    st.line_chart(AREA_df1)
    if st.checkbox('Show dataframe'):
        st.dataframe(AREA_df1)


def DETECT():
    st.video('C:\\Users\\kyjoo\\Desktop\\산학자료\\code\\streamlit\\detect.mp4')


options = st.sidebar.selectbox('센서데이터', ['main', 'MFL', 'AREA', 'DETECT'])

if options == 'main':
    main()
elif options == 'MFL':
    MFL()
elif options == 'AREA':
    AREA()
elif options == 'DETECT':
    DETECT()
