
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
import src.pages.Import_Data as importdata

st.markdown("# Check Duplicates ")
st.sidebar.markdown("# Check Duplicates-")

df = importdata.load_page()
option = st.selectbox(
     'Select the dataset you want to check',
     (df1, df2, df3, df4, df5))
st.write('You selected:', option)
