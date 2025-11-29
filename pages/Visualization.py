import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 데이터 시각화")

df = pd.read_excel("SEco.xlsx")

fig = px.box(df, x="장르", y="SEco_norm", title="장르별 위험도 분포")
st.plotly_chart(fig)

month_fig = px.line(df.groupby("MONTH")["SEco_norm"].mean().reset_index(),
                    x="MONTH", y="SEco_norm",
                    title="월별 평균 위험도")
st.plotly_chart(month_fig)
