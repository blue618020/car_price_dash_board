import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_app_eda():
    st.subheader('데이터 분석')

    df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')
    print(df)

    if st.checkbox('데이터 프레임 보기'):
        st.dataframe(df)


    # 아래서부턴 구글코랩에서 분석했던걸 여기로 가져오는 작업!

    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())  



    st.subheader('최대 / 최소 데이터 확인하기')
    column = st.selectbox('컬럼을 선택하세요.', df.columns[3:]) 
    # 0~2 까지는 문자열이라 제외
    
    st.text('최대값 데이터')
    st.dataframe(df.loc[df[column] == df[column].max(), ]) # 최대값
    st.text('최소값 데이터')
    st.dataframe(df.loc[df[column] == df[column].min(), ]) # 최소값



    st.subheader('컬럼 별 히스토그램')
    column = st.selectbox('히스토그램을 확인할 컬럼을 선택하세요', df.columns)
    bins = st.number_input('bins의 개수를 입력하세요.', 10, 30, 20) # ,시작,끝,기본값
    
    fig = plt.figure() # 차트 생성
    df[column].hist(bins=bins)

    plt.title(column + 'Histogram')
    plt.xlabel(column)
    plt.ylabel('count')
    st.pyplot(fig)
    


    st.subheader('상관 관계 분석')
    column_list = st.multiselect('상관분석 하고싶은 컬럼을 선택하세요',df.columns[3:])
    # df[column_list].corr() # 유저가 선택한 컬럼을 가져와서 .corr() 실행

    if len(column_list) > 1: # 유저가 컬럼을 1개이상 선택했다면 차트 보이게 하기
        fig2 = plt.figure()
        sns.heatmap(data = df[column_list].corr(), annot=True, 
                vmin=-1, vmax=1, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        st.pyplot(fig2) 
