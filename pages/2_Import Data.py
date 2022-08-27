
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


st.markdown("# Import Data ")
#st.sidebar.markdown("# Import Data-")

datatab1, datatab2, datatab3, datatab4, datatab5 = st.tabs(["Dataset 1","Dataset 2", "Dataset 3", "Dataset 4","Dataset 5"])

with datatab1:
    st.markdown('Select your data file')
    df1 = st.file_uploader("Choose a file", key='df1')
    dataset1 = st.text_input('Enter name of dataset', 'dataset1')

with datatab2:
    st.markdown('Select your data file')
    df2 = st.file_uploader("Choose a file", key='df2')
    dataset2 = st.text_input('Enter name of dataset', 'dataset2')

with datatab3:
    st.markdown('Select your data file')
    df3 = st.file_uploader("Choose a file", key='df3')
    dataset3 = st.text_input('Enter name of dataset', 'dataset3')

with datatab4:
    st.markdown('Select your data file')
    df4 = st.file_uploader("Choose a file", key='df4')
    dataset4 = st.text_input('Enter name of dataset', 'dataset4')

with datatab5:
    st.markdown('Select your data file')
    df5 = st.file_uploader("Choose a file", key='df5')
    dataset5 = st.text_input('Enter name of dataset', 'dataset5')
