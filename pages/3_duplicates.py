
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

#df = importdata.load_page()
if st.session_state['df1'] is not None:
     try:
          data1 = pd.read_csv(st.session_state['df1'])
     except Exception as e:
          print(e)
          data1 = pd.read_excel(st.session_state['df1'])
     st.write(data1)

option = st.selectbox(
     'Select the dataset you want to check',
     (data1, "data2"))
st.write(option)
st.write(st.session_state['df1'])