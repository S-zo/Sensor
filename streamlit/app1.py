from matplotlib import colors as mcolors  # 두번째 프로토타입
import matplotlib.pyplot as plt  # 대시보드
from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d import Axes3D
import streamlit.components.v1 as components
import altair as alt
import streamlit as st
import numpy as np
import pandas as pd
import comedata as cd
import matplotlib.animation as animation
import cv2
# from streamlit_webrtc import webrtc_streamer


MFL_df = cd.MFLdf
AREA_df = cd.AREAdf
MFL_df1 = MFL_df.drop('id', axis=1)
AREA_df1 = AREA_df.drop('id', axis=1)
video_file = open(
    'C:\\Users\\kyjoo\\Desktop\\smartinside\\code\\streamlit\\demo_output.mp4', 'rb')
video_bytes2 = video_file.read()
video_file = open(
    "C:\\Users\\kyjoo\\Desktop\\smartinside\\code\\gitadd\\streamlit\\workman.mp4", 'rb')
video_bytes = video_file.read()


def main():
    st.title("건설안전-작업자현황 및 안전감시 시스템")
    st.write("\n")
    cols = st.beta_columns(4)
    cols[0].write("현재 작업인원: {}".format(20))
    cols[1].write("경고(2명이상): {}".format("삐용"))

    st.sidebar.markdown(f'''
        <div class="card text-white bg-info mb-3" style="width: 18rem">
            <div class="card-body">
                <h5 class="card-title">Total Worker : {20}\n</h5>
                <h5 class="card-text">Warning : {1}</h5>
            </div>
        </div>''', unsafe_allow_html=True)

    if 3 >= 2:
        st.warning("작업환경이 위험합니다.")

    fig = plt.figure(figsize=(22, 3))

    times_work = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    tn_work = [15, 16, 15, 14, 15, 16, 17, 18, 17, 17, 14, 6]
    tn_warn = [1, 1, 1, 2, 3, 4, 3, 2, 0, 1, 1, 1]
    ax = fig.add_subplot(1, 2, 1)
    bx = fig.add_subplot(1, 2, 2)
    ax.bar(
        times_work,
        tn_work
    )
    bx.bar(
        times_work,
        tn_warn
    )
    bx.set_xlabel("time")
    bx.set_ylabel("warning")
    ax.set_xlabel("time")
    ax.set_ylabel("workers")

    st.pyplot(fig)


def MFL():
    st.title("MFL Data")
    st.write("\n")
    # sensor_list = MFL_df1.columns.unique()
    # sensors = st.multiselect(
    #     "센서 선택", list(sensor_list)), [
    #         sensor_list[0], sensor_list[1]]

    st.line_chart(MFL_df1)
    if st.checkbox('Show dataframe'):
        st.dataframe(MFL_df1)


def AREA():
    st.title("AREA Data")
    st.write("\n")

    st.line_chart(AREA_df1)
    if st.checkbox('Show dataframe'):
        st.dataframe(AREA_df1)


def DETECT():
    st.title("DETECTING")

    st.video(video_bytes)


options = st.sidebar.selectbox('센서데이터', ['PROJECT', 'MFL', 'AREA', 'DETECT'])

if options == 'PROJECT':
    main()
elif options == 'MFL':
    MFL()
elif options == 'AREA':
    AREA()
elif options == 'DETECT':
    DETECT()


if st.sidebar.button("작업장"):
    st.video(video_bytes2)

# if st.sidebar.button("커멘드"):
#     run = st.checkbox('Run')
#     FRAME_WINDOW = st.image([])
#     camera = cv2.VideoCapture(0)
#     while run:
#         _, frame = camera.read()
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         FRAME_WINDOW.image(frame)
#     else:
#         webrtc_streamer(key="example")
