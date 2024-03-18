import pandas as pd
import streamlit as st
import time

df = pd.read_csv('D:\\Coding journey 2024\\datascience\\stremlit\\startup_funding.csv')
st.dataframe(df)