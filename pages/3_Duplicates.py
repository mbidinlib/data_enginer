
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
     except Exception as e:
          print(e)
          st.dataframe(pd.read_excel(StringIO(df1)))

     
if "dfa1" not in st.session_state or "dfa2" not in st.session_state:
     st.markdown("Go to the import page to import your dataset(s)")

