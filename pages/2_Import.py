
'''
Date: Wed Aug 23 21:12:18 2022
@author: Glooory
Purpose: Data Engineering
'''

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import time as tm
from persist import persist, load_widget_state
#from streamlit_multipage import MultiPage


st.markdown("# Import Data ")
#st.sidebar.markdown("# Import Data-")

datatab1, datatab2, datatab3, datatab4, datatab5 = st.tabs(["Dataset 1","Dataset 2", "Dataset 3", "Dataset 4","Dataset 5"])

with datatab1:
    st.markdown('Select your data file')
    dfa1 = st.file_uploader("Choose a file", key=persist('df1'))
    if dfa1:
        if 'pd.read_csv' in st.session.state:
            df1=st.session_state.pd.read_csv   
        else:
            try:
                df1 = pd.read_csv(dfa1)
            except Exception as e:
                print(e)
                df1 = pd.read_excel(dfa1)
            st.write(df1)
            
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
