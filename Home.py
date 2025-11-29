import streamlit as st

st.set_page_config(page_title="SEco Dashboard", layout="wide")

st.title(" SEco : 올림픽공원 공연 위험도 예측 시스템 ")
st.markdown("""
### 👋 올공지기 웹사이트에 오신 것을 환영합니다 👋


이 웹사이트는 **공연장 환경·안전 지표 (SVI, HLI, AQHI)**를 기반으로  
- 공연장 혼잡도  
- 장르 특성  
- 관람 인원  
- 계절 요인  

등을 통합 분석하여 **공연 위험도를 예측**하는 모델입니다.

---

### 📌 우리는요...
- **모델 설명** — SEco 알고리즘 및 데이터 처리 구조 
- **예측 모델** — Streamlit 기반 UI로 빠른 위험도 예측  
- **데이터 시각화** — 월별 전체 위험 시계열/Heatmap, 공연별 위험도 막대그래프, SVI / HLI / AQHI의 월별 비교 그래프, 위험등급 분포 Pie chart 
""")
