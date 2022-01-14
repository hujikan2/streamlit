import pandas as pd
import streamlit as st
import numpy as np

st.title("Getting to Know Your Data")
st.markdown("-----------")

upload_file = st.file_uploader("Upload Your Dataset")

# Read Dataset
if upload_file is None:
    def get_data_from_csv():
        # To Read Files
        df = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/nbaallelo.csv')
        return df
    df = get_data_from_csv()

# Show dataset
if upload_file is None:
    if st.checkbox("Preview Your Dataset"):
        if st.button("Head"):
            st.write("Menampilkan 5 Data Teratas")
            st.write(df.head())
        if st.button ("Tail"):
            st.write("Menampilkan 5 Data Terbawah")
            st.write(df.tail())
