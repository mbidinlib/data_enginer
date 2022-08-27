
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

#st.sidebar.markdown("# Home page")

st.markdown("# MGlory Data Engineering Tolkit ")
st.markdown("Welcome to MGlory Data Engineering toolkit.\
    This is a python based tool that would help you prepare your dataset for analysis.\
    The tool contains the following components:\
    ")
st.markdown("## Data Import")
st.markdown("With the data import page, you would be able to import upto five (5) datasets for your work.\
    Each dataset is in a seperate tab and you can navigate across tabs")
