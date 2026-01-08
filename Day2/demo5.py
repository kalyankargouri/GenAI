import pandas as pd
import streamlit as st
st.title("csv explorer")
data_file=st.file_uploader("upload a csv file",type=["csv"])
if data_file:
    df=pd.read_csv(data_file)
    st.dataframe(df)