import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor

st.title("🔮 공연 위험도 예측")

@st.cache_resource
def train_model():
    # 1) 데이터 불러오기
    df = pd.read_excel("SEco.xlsx")

    # 2) Feature / Label
    X = df[['공연장', '장르', '관람인원', 'MONTH']]
    y = df['SEco_norm']   # 또는 'AV-HSI' 쓰고 싶으면 여기만 바꾸면 됨

    # 3) 전처리 설정
    categorical = ['공연장', '장르']
    numeric = ['관람인원', 'MONTH']

    preprocess = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown="ignore"), categorical),
        ('num', 'passthrough', numeric)
    ])

    # 4) 파이프라인 모델
    model = Pipeline([
        ('preprocess', preprocess),
        ('regressor', XGBRegressor(
            n_estimators=300,
            learning_rate=0.1,
            max_depth=5,
            random_state=42
        ))
    ])

    # 5) 학습 (train/test 굳이 안 나눠도 되지만 깔끔하게만)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model.fit(X_train, y_train)

    # 카테고리 목록도 같이 반환 (드롭다운용)
    halls = X['공연장'].unique().tolist()
    genres = X['장르'].unique().tolist()
    return model, halls, genres

# 🔁 페이지 처음 열릴 때 한 번만 학습됨 (캐시)
model, hall_list, genre_list = train_model()

# ==== 입력 UI ====
hall = st.selectbox("공연장", hall_list)
genre = st.selectbox("장르", genre_list)
audience = st.slider("관람인원", 100, 100000, 100, step=100)
month = st.selectbox("월", list(range(1, 13)))

if st.button("예측하기"):
    new_data = pd.DataFrame(
        [[hall, genre, audience, month]],
        columns=['공연장', '장르', '관람인원', 'MONTH']
    )

    pred = model.predict(new_data)[0]

    # 위험 등급
    if pred >= 81:
        label = "🚨 5단계 (위험)"
    elif pred >= 61:
        label = "⚡ 4단계 (경계)"
    elif pred >= 41:
        label = "⚠️ 3단계 (주의)"
    elif pred >= 21:
        label = "🌿 2단계 (양호)"
    else:
        label = "🌳 1단계 (안전)"

    st.subheader("📌 예측 결과")
    st.write(f"**AV-HSI 예측치:** {pred:.2f}")
    st.write(f"**위험 등급:** {label}")
