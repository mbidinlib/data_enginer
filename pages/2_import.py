
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
#from streamlit_multipage import MultiPage
from streamlit_pandas_profiling import st_profile_report
from streamlit import session_state as session
from pandas_profiling import ProfileReport


st.markdown("# Import Data ")
#st.sidebar.markdown("# Import Data-")

datatab1, datatab2, datatab3, datatab4, datatab5 = st.tabs(["Dataset 1","Dataset 2", "Dataset 3", "Dataset 4","Dataset 5"])

with datatab1:

    def get_profile_report(file_info, df):
        pr = ProfileReport(df, explorative=True, lazy=True, minimal=True)
        return pr

    def profiler():
        delim = session.delim
        file = st.session_state.upload
        delimiter = delim.split(" ")[1][1:-1]
        df = pd.read_csv(file, sep=delimiter, engine="python")
        file_info = {"Filename": file.name, "FileType": file.type, "FileSize": file.size}
        st.write(file_info)
        pr = get_profile_report(file_info, df)
        st_profile_report(pr)

        def data_uploader_form():
            file_upload_form = st.form(key="file_upload")
            with file_upload_form:
                data_file = st.file_uploader("Upload File", type=['csv', 'xlsx'], key="upload")
                delim_list = ["pipe (|)", r"tab (\t)", "comma (,)", "semicolon (;)"]
                delim = st.selectbox("Select File Seperator/Delimiter", delim_list, key="delim")
                file_upload_form.form_submit_button(label='Profile Data', on_click=profiler)


    '''
    st.markdown('Select your data file')
    dfa1 = st.file_uploader("Choose a file",type=['csv', 'xlsx'], key='df1')
    if dfa1 is not None:
        try:
            df1 = pd.read_csv(dfa1)
        except Exception as e:
            print(e)
            df1 = pd.read_excel(dfa1)
        st.write(df1)
    '''
with datatab2:
    st.markdown('Select your data file')
    dfa2 = st.file_uploader("Choose a file", key='df2')
    if dfa2 is not None:
        df2 = pd.read_csv(dfa2)
        st.write(df2)


with datatab3:
    st.markdown('Select your data file')
    dfa3 = st.file_uploader("Choose a file", key='df3')
    if dfa3 is not None:
        df3 = pd.read_csv(dfa3)
        st.write(df3)

with datatab4:
    st.markdown('Select your data file')
    dfa4 = st.file_uploader("Choose a file", key='df4')
    if dfa4 is not None:
        df4 = pd.read_csv(dfa4)
        st.write(df4)

with datatab5:
    st.markdown('Select your data file')
    dfa5 = st.file_uploader("Choose a file", key='df5')
    if dfa5 is not None:
        df5 = pd.read_csv(dfa5)
        st.write(df5)
