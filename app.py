import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from app_home import run_app_home
from app_eda import run_app_eda
from app_ml import run_app_ml

def main():

    # 화면 구조 잡기
    st.title('자동차 가격 예측 앱')
    
    # 1. 사이드바 만들기
    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴',menu)  # 유저가 선택한 3개의 meun 중 하나가 choice 변수에 들어감
    
    if choice == menu[0]:
        # 따로 파일에 분리한 작동내용 호출
        run_app_home()

    elif choice == menu[1]:
        # 따로 파일에 분리한 작동내용 호출
        run_app_eda()

    else : 
        run_app_ml()

    

if __name__ == '__main__':
    main()