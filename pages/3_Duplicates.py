
'''
Date: Wed Aug 23 21:12:18 2022
@author: Glooory
Purpose: Data Engineering
'''

from io import StringIO
import pandas as pd
import streamlit as st

#Import pages
#from streamlit_multipage import MultiPage


st.markdown("# Check Duplicates ")
st.sidebar.markdown("# Check Duplicates-")

if "dfa1" in st.session_state or "dfa2" in st.session_state:
     df1= st.session_state["dfa1"]
     select_df = st.selectbox(
          'Select the dataset you want to check',
          ([df1,df2]))
     try:             
          st.dataframe(pd.read_csv(StringIO(df1)))
     except:
          st.dataframe(pd.read_excel(StringIO(df1)))

     




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