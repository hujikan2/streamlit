import pandas as pd
import streamlit as st
import numpy as np

st.title("Getting to Know Your Data")
st.markdown("-----------")

# ---- SIDEBAR ----
st.sidebar.header("Please Upload Data Here: :open_file_folder:")
uploaded_file = st.sidebar.file_uploader("Upload Your Dataset")

# ----- Read Dataset ----
if uploaded_file is not None:
    def get_data_from_csv():
        # To Read Files
        data = pd.read_csv(uploaded_file)
        return data
    data = get_data_from_csv()

# -- Show Dataset -- 
if uploaded_file is not None:
    st.subheader("Viewing data")
    st.write("See the Basics section.")
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write('Menampilkan 5 dataset teratas')
            st.write(data.head())
        if st.button("Tail"):
            st.write('Menampilkan 5 dataset terbawah')
            st.write(data.tail())

# -- Show Basics Statistic Summary --
if uploaded_file is not None:
    st.write("See know statistic your data")
    if st.checkbox("Shows a quick statistic summary of your data:"):
        st.write(data.describe().transpose())

# -- Selection Data --
if uploaded_file is not None:
    st.subheader("Selection by label")
    select = data.loc[:0]
    if st.checkbox("Section using a label"):
        st.write(select)
        st.write("Using .loc[:0]")
    st.subheader("Selection by position")
    position = data.iloc[3:5, 0:2]
    if st.checkbox("Selection using a position"):
        st.write(position)
        st.write("Using .iloc[3:5, 0:2]")

# -- Missing data --
if uploaded_file is not None:
    st.subheader("Missing data")
    if st.checkbox("Get know your missing data"):
        st.write(data.isna().sum())
        st.write("Lihat Keseluruhan apakah ada missing value terhadap data yang anda sajikan. Kalau iya alakukan untuk handle missing value tersebut.")