# :house_with_garden: 맨하탄 주택 가격 프로젝트 :heavy_dollar_sign:
## 프로젝트 개요
이 프로그램은 맨하탄에 있는 주택 데이터셋을 활용하여 사용자가 원하는 주택의 옵션을 선택하면 그 선택한 옵션을 고려한 주택의 예상 가격을 알려주는 프로그램입니다.

## 사용된 프로그램
* Streamlit
* Pandas
* joblib
* seaborn
* pyplot
## 프로그램 실행 및 사용방법
1. 깃허브에서 'Download ZIP'을 이용해서 해당 폴더를 다운받고, 'Streamlit_PricePredict.py'파일을 실행시킵니다.
2. Terminal에서 streamlit 파일을 실행시켜 주택 가격 프로그램 웹페이지에 접속합니다.
3. 웹페이지에서 본인이 원하는 주택의 옵션을 선택합니다.
4. 옵션 선택이 완료되면 '가격 예측하기' 버튼을 클릭해 해당 주택의 가격을 측정합니다.

## 요소들에 관한 설명과 사용법
* 침실의 개수, 욕실의 개수 : 0 ~ 5개 (number_input 함수 사용)
* 주택의 면적(단위=ft²) : 250 ~ 4800 (slider, number_input 함수 사용)
* 지하철역까지 걸리는 시간(단위=분) : 0 ~ 43 (slider, number_input 함수 사용)
* 주택의 층 수 : 0 ~ 83 (slider, number_input 함수 사용)
* 건물의 연식 : 0 ~ 180 (slider, number_input 함수 사용)
* 중계 수수료 지불 의향 : ('Yes' 또는 'No' 선택 가능, selectbox 함수 사용)
* 건물 내부 옵션 선택 구현

  - 루프덱(옥상 테라스)
  - 세탁기와 건조기
  - 도어맨
  - 엘리베이터
  - 식기 세척기
  - 헬스장
#### 이상 위의 옵션들은 checkbox 함수를 사용하여 다중 선택 가능하도록 구현
* 위의 옵션들의 설정을 완료한 후 '가격 예측하기' 버튼을 클릭하면 내가 원하는 옵션을 가진 주택의 예상 가격이 나옴

![맨하탄_주택가격1](https://github.com/user-attachments/assets/5cf82998-43e8-4708-9fd6-0b0b39a91a29) ![맨하탄_주택가격2](https://github.com/user-attachments/assets/320d2b05-aae0-4a55-a4ef-a03329e8ecd5)
