import streamlit as st
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt


st.title('맨하탄주택가격예측:heavy_dollar_sign:')

with st.expander('요소들에 대한 설명'):
    list = ['bedrooms: 침실의 개수', 'bathrooms: 욕실의 개수', 'size_sqft: 주택의 면적(제곱피트 단위)', 'min_to_subway: 지하철역까지의 거리(분 단위)', 'floor: 주택의 층수',
        'building_age_yrs: 건물의 연식', 'no_fee: 중개 수수료 여부', 'has_roofdeck: 루프덱(옥상 테라스)이 있는지 여부 (1 = 있음, 0 = 없음)',
        'has_washer_dryer: 세탁기와 건조기가 있는지 여부 (1 = 있음, 0 = 없음)', 'has_doorman: 도어맨이 있는지 여부 (1 = 있음, 0 = 없음)', 'has_elevator: 엘리베이터가 있는지 여부 (1 = 있음, 0 = 없음)',
        'has_dishwasher: 식기세척기가 있는지 여부 (1 = 있음, 0 = 없음)', 'has_gym: 헬스장이 있는지 여부 (1 = 있음, 0 = 없음)']
    for i in list:
        st.caption(i)

# 'bedrooms': number_input, 'bathrooms': number_input, 'size_sqft': number_input or slider, 'min_to_subway': number_input, 'floor': number_input or slider
# 'building_age_yrs': number_input, 'no_fee': selectbox, 'has_roofdeck': selectbox, 'has_washer_dryer': selectbox, 'has_doorman':selectbox
# 'has_elevator': selectbox, 'has_dishwasher': selectbox, 'has_gym': selectbox
with st.expander('요소 시각화'):
    #시각화
    house = pd.read_csv('맨하탄주택가격.csv',encoding='cp949')
    tab1, tab2 = st.tabs(['Heatmap', 'Bar chart'])

    with tab1:    
        # 상관계수 계산
        corr = house[['rent', 'bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_gym']].corr()

        # 히트맵 그리기
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f', ax=ax)
        ax.set_title('Correlation Heatmap')

        # Streamlit에 표시
        st.pyplot(fig)

    with tab2:
        # 수치형 피처 목록
        numeric_features = ['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 
                            'floor', 'building_age_yrs']

        # 평균 rent 계산
        mean_rents = [house.groupby(feature)['rent'].mean().mean() for feature in numeric_features]

        # 바 차트 그리기
        plt.figure(figsize=(10, 6))
        plt.barh(numeric_features, mean_rents, color='skyblue')
        plt.title('Average Rent by Feature')
        plt.xlabel('Average Rent ($)')
        plt.ylabel('Features')
        plt.grid(axis='x')

        # Streamlit에서 Matplotlib 차트 표시
        st.pyplot(plt)

# 요소 선택
bedrooms = st.number_input(label=':green[침실]의 개수를 입력하세요.',
                min_value=0,
                max_value=5)

bathrooms = st.number_input(label=':green[욕실]의 개수를 입력하세요.',
                min_value=0,
                max_value=5)

# 세션 상태 초기화
if 'area' not in st.session_state:
    st.session_state.area = 1000
if 'subway_time' not in st.session_state:
    st.session_state.subway_time = 20
if 'floor' not in st.session_state:
    st.session_state.floor = 10.0
if 'building_age' not in st.session_state:
    st.session_state.building_age = 50

# Number Input의 값을 슬라이더와 동기화하는 함수
def update_slider(key):
    st.session_state[key] = st.session_state[f'{key}_input']

# Slider의 값을 Number Input과 동기화하는 함수
def update_input(key):
    st.session_state[f'{key}_input'] = st.session_state[key]

# 컬럼 생성 및 슬라이더, number_input 추가
# 1. 주택 면적
col1, col2 = st.columns([3, 1])
with col1:
    st.slider('주택의 :green[면적]을 정해주세요. (단위: ft²)', 250, 4800, step=1, key='area', on_change=update_input, args=('area',))
with col2:
    st.number_input(' ', min_value=250, max_value=4800, step=1, key='area_input', on_change=update_slider, args=('area',))
st.write(f"선택한 주택 :green[면적]은 {st.session_state.area} ft²입니다.")

# 2. 지하철역까지 걸리는 시간
col1, col2 = st.columns([3, 1])
with col1:
    st.slider('지하철역까지 걸리는 :green[시간](단위: 분)', 0, 43, step=1, key='subway_time', on_change=update_input, args=('subway_time',))
with col2:
    st.number_input(' ', min_value=0, max_value=43, step=1, key='subway_time_input', on_change=update_slider, args=('subway_time',))
st.write(f"지하철역까지 걸리는 :green[시간]은 {st.session_state.subway_time}분입니다.")

# 3. 주택의 층 수
col1, col2 = st.columns([3, 1])
with col1:
    st.slider('주택의 :green[층 수]를 정해주세요.', 0.0, 83.0, step=0.5, key='floor', on_change=update_input, args=('floor',))
with col2:
    st.number_input(' ', min_value=0.0, max_value=83.0, step=0.5, key='floor_input', on_change=update_slider, args=('floor',))
st.write(f"선택한 주택 :green[층 수]는 {st.session_state.floor}층입니다.")

# 4. 건물의 연식
col1, col2 = st.columns([3, 1])
with col1:
    st.slider('건물의 :green[연식]을 정해주세요.', 0, 180, step=1, key='building_age', on_change=update_input, args=('building_age',))
with col2:
    st.number_input(' ', min_value=0, max_value=180, step=1, key='building_age_input', on_change=update_slider, args=('building_age',))
st.write(f"건물의 :green[연식]은 {st.session_state.building_age}년입니다.")

no_fee = st.selectbox(':green[중계 수수료]를 지불할 의향이 있으신가요?', ('Yes','No'), index=1)

#################### 옵션 선택 구현 #######################

# 질문 표시
st.write('건물에 원하는 :green[옵션]을 선택해주세요.')

# 체크박스 생성
roofdeck = st.checkbox('루프덱(옥상 테라스)')
washer_dryer = st.checkbox('세탁기와 건조기')
doorman = st.checkbox('도어맨')
elevator = st.checkbox('엘리베이터')
dishwasher = st.checkbox('식기세척기')
gym = st.checkbox('헬스장')

# 선택된 옵션을 담을 리스트
selected_options = []

# 각각의 체크박스가 선택되었는지 확인하고 리스트에 추가
if roofdeck:
    selected_options.append('루프덱')
if washer_dryer:
    selected_options.append('세탁기와 건조기')
if doorman:
    selected_options.append('도어맨')
if elevator:
    selected_options.append('엘리베이터')
if dishwasher:
    selected_options.append('식기세척기')
if gym:
    selected_options.append('헬스장')

# 선택된 옵션에 따라 메시지 출력
if len(selected_options) > 0:
    # 선택한 옵션이 1개일 때, 옵션만 출력
    if len(selected_options) == 1:
        st.write(f"{selected_options[0]}을(를) 선택하셨습니다.")
    # 선택한 옵션이 2개일 때, "과"를 사용
    elif len(selected_options) == 2:
        st.write(f"{selected_options[0]}와(과) {selected_options[1]}을(를) 선택하셨습니다.")
    # 선택한 옵션이 3개 이상일 때, 마지막 옵션 앞에 "그리고"를 사용
    else:
        selected_message = ", ".join(selected_options[:-1]) + f" 그리고 {(selected_options[-1])}을(를) 선택하셨습니다."
        st.write(selected_message)
else:
    st.write('옵션을 선택하지 않으셨습니다.')

# 가격 예측
predict = st.button('가격 예측하기')
if predict:
    features = [[bedrooms, bathrooms, st.session_state.area, st.session_state.subway_time, st.session_state.floor, st.session_state.building_age, not no_fee, roofdeck, washer_dryer, doorman, elevator, dishwasher, gym]]

    # 모델 로드
    rf_loaded = joblib.load('random_forest_model.joblib')

    # 로드된 모델로 예측
    predictions = rf_loaded.predict(features)
    st.success(f'예측한 주택 가격은 {round(predictions[0], 2)}$ 입니다!')