
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

#Import pages
#from streamlit_multipage import MultiPage


st.markdown("# Check Duplicates ")
st.sidebar.markdown("# Check Duplicates-")

#Call datasets imported from import
data1 = st.session_state['file']
st.write(data1)

'''
if st.session_state['df2'] is not None:
     try:
          data2 = pd.read_csv(st.session_state['df2'])
     except Exception as e:
          print(e)
          data2 = pd.read_excel(st.session_state['df2'])

if st.session_state['df3'] is not None:
     try:
          data3 = pd.read_csv(st.session_state['df3'])
     except Exception as e:
          print(e)
          data3 = pd.read_excel(st.session_state['df3'])

if st.session_state['df4'] is not None:
     try:
          data4 = pd.read_csv(st.session_state['df4'])
     except Exception as e:
          print(e)
          data4 = pd.read_excel(st.session_state['df4'])

if st.session_state['df5'] is not None:
     try:
          data5 = pd.read_csv(st.session_state['df5'])
     except Exception as e:
          print(e)
          data5 = pd.read_excel(st.session_state['df5'])


select_df = st.selectbox(
     'Select the dataset you want to check',
     (data1))
st.write(select_df)
'''