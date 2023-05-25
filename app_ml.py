import streamlit as st
import numpy as np
import joblib

def run_app_ml():
    st.subheader('자동차 금액 예측')

    # 성별, 나이, 연봉, 카드빚, 자산을 유저에게 입력받기
    # 인공지능 학습을 위 목록으로만 했으니깐
    gender = st.radio('성별 선택', ['남자', '여자'])
    if gender == '남자':
        gender = 0  # 여기서 0 또는 1로 바꿔주기(컴퓨터가 알아듣게)
    else:
        gender = 1
    
    age = st.number_input('나이 입력', 18, 100)

    salary = st.number_input('연봉 입력', 5000, 1000000)

    debt = st.number_input('카드빚', 0, 1000000)

    worth= st.number_input('자산 입력', 1000, 10000000)



    # 버튼을 누르면 예측한 금액을 표시하기
    # model/regressor.pkl 파일은 구글 코랩에서 만들었던 인공지능 파일
    if st.button('금액 예측'):
        new_data = np.array([gender, age, salary, debt, worth])
        new_data = new_data.reshape(1,5) # 2차원으로 변경 

        regressor = joblib.load('model/regressor (1).pkl')  # dump의 반대는 load
        y_pred = regressor.predict(new_data)
        print(y_pred) # 잘 돌아가는지 확인


        # 리스트로 출력하지 말고 숫자만 빼오기
        print(y_pred[0])

        price = round(y_pred[0]) # 소수점 빼버리기
        print(str(price) + '달러짜리 차량 구매 가능합니다.') # 문자열도 추가해보고

        # 최종 출력
        st.text(str(price) + '달러짜리 차량 구매 가능합니다.')  
