
'''
Date: Wed Aug 23 21:12:18 2022
@author: Glooory
Purpose: Data Engineering
'''
import streamlit as st
import SessionState
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from persist import persist, load_widget_state
from io import StringIO


st.markdown("# Import Data ")
#st.sidebar.markdown("# Import Data-")

datatab1, datatab2, datatab3, datatab4, datatab5 = st.tabs(["Dataset 1","Dataset 2", "Dataset 3", "Dataset 4","Dataset 5"])

with datatab1:
    st.markdown('Select your data file')
    dfa1 = st.file_uploader("Choose a file",type = "csv", key=persist('df1'))
    if dfa1:
        if 'df1a' not in st.session.state:
            st.session_state["dfa1"]= dfa1.getvalue().decode("utf-8")
        if 'df1a' in st.session.state:
            st.dataframe(pd.read_csv(StringIO(st.session_state["dfa1"])))           
with datatab2:
    st.markdown('Select your data file')
    dfa2 = st.file_uploader("Choose a file", key=persist('df2'))
    if dfa2 is not None:
        df2 = pd.read_csv(dfa2)
        st.write(df2)


with datatab3:
    st.markdown('Select your data file')
    dfa3 = st.file_uploader("Choose a file", key=persist('df3'))
    if dfa3 is not None:
        df3 = pd.read_csv(dfa3)
        st.write(df3)

with datatab4:
    st.markdown('Select your data file')
    dfa4 = st.file_uploader("Choose a file", key=persist('df4'))
    if dfa4 is not None:
        df4 = pd.read_csv(dfa4)
        st.write(df4)

with datatab5:
    st.markdown('Select your data file')
    dfa5 = st.file_uploader("Choose a file", key=persist('df5'))
    if dfa5 is not None:
        df5 = pd.read_csv(dfa5)
        st.write(df5)
