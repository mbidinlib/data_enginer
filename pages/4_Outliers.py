
'''
Date: Wed Aug 23 21:12:18 2022
@author: Glooory
Purpose: Data Engineering
'''

from io import StringIO
import pandas as pd
import streamlit as st
from scipy import stats
import numpy as np
#from streamlit_multipage import MultiPage


st.markdown("# Check Outliers")
st.sidebar.markdown("# Check Outliers-")



col1, col2 = st.columns((1,2))

if ("dataset1" in st.session_state or "dataset2" in st.session_state or "dataset3" in st.session_state or 
     "dataset4" in st.session_state or "dataset4" in st.session_state or "dup_drop_data" in st.session_state):
    
     #Get short name of datasets
     #############################
     #Dataset 1
     if "dataset1" not in st.session_state:
          ds1=""
     else:
          try:
               ds1 = st.session_state["dataset1_name"]
          except:
               ds1 = "dataset1"
     #Dataset 2
     if "dataset2" not in st.session_state:
          ds2=""
     else:
          try:
               ds2 = st.session_state["dataset2_name"]
          except:
               ds2 = "dataset2"
     #Dataset 3
     if "dataset3" not in st.session_state:
          ds3=""
     else:
          try:
               ds3 = st.session_state["dataset3_name"]
          except:
               ds3 = "dataset3"
     #Dataset 4
     if "dataset4" not in st.session_state:
          ds4=""
     else:
          try:
               ds4 = st.session_state["dataset4_name"]
          except:
               ds4 = "dataset4"
     #Dataset 5
     if "dataset5" not in st.session_state:
          ds5=""
     else:
          try:
               ds5 = st.session_state["dataset5_name"]
          except:
               ds5 = "dataset5"
     #Deduplicated-data
     if "dup_drop_data" not in st.session_state:
          dsdup=""
     else:
          try:
               dsdup = st.session_state["dupdrop_name2"]
          except:
               dsdup = "dup_drop_data"



     with col1:
          #Selecting dataset to use
          ###########################
          sel_df = st.selectbox(
               'Select the dataset you want to check',
               [ds1, ds2, ds3, ds4, ds5, dsdup])
          if sel_df == ds1 :
               selected_df = "dataset1" 
          elif sel_df == ds2:
               selected_df = "dataset2"
          elif sel_df == ds3:
               selected_df = "dataset3"
          elif sel_df == ds4:
               selected_df = "dataset4"
          elif sel_df == ds5:
               selected_df = "dataset5"
          elif sel_df == dsdup:
               selected_df = "dup_drop_data"


          if sel_df != "":
               master_data = st.session_state[selected_df]

               # Check duplicates
               ##################
               with st.expander("Check Outliers",expanded=False):
                         out_data_vars = master_data.columns
                         out_id = st.multiselect("Select variable you want to checkoutliers on. This can also be a combination of variables",out_data_vars)
                         if out_id:
                            
                            out_mult_e = st.number_input("Optional: Enter the multiplier/threshold value", help = 
                            "The default is 3.0 since `99.7%` of the data points lie between +/- 3 standard deviation (using Gaussian Distribution approach)")
                              # Query duplicates:
                            if out_mult_e:
                                out_mult = out_mult_e
                            else: 
                                out_mult_e
                            sel_logic = st.selectbox(
                                'For multiple variables: Select logical operator(defailt is |)', ["&", "|"], help = 
                                """
                                If you selected more than one variable, & would flag observations with outliers 
                                in all the specified variables while | would flag observations that have outliers inat least 
                                one of the specified variables""")
                            if sel_logic:
                                logic_op = sel_logic
                            else :
                                logic_op = "|"

                            outvar_len = len(out_data_vars)
                            out_join = ""
                            if outvar_len > 1 :
                                for j in range(outvar_len):
                                    outvar = out_data_vars[j]
                                    z = "np.abs(stats.zscore(master_data[{outvar}]))" 

                                    if j == 1:
                                        outcond = "np.where( ({z} > {out_mult_e}) {logic_op} "
                                    else:
                                        outcond = " {logic_op} ({z} > {out_mult_e})"
                                    out_join = out_join + outcond 
                                out_join = out_join + ")"
                            else: 
                                z = "np.abs(stats.zscore(master_data[{out_data_vars}]))"
                                out_join = "np.where( ({z} > {out_mult_e}) )"

                            
                            st.write(out_join)
                            out_data = out_join
                              
                              
                              # Add buttons
                            check_out = st.button('Flag Outliers', key= 'check_out')
                              
                              # Create a Pandas Excel writer using XlsxWriter as the engine.

                            out_data_down = out_data.to_csv().encode('utf-8')
                            st.download_button(label = 'Export Outliers', data = out_data_down, 
                                   file_name = 'duplicates.csv', mime = 'text/cvs')      
               


               # Resolve Outliers
               with st.expander("Resolve Outliers",expanded=False):
                    
                    #Define Action buttons
                    dropvals = st.button('Drop Values', key= 'keepfirst', help=
                    "This would drop only the outlier values")
                    dropobs= st.button('Keep Last', key= 'keeplast', help=
                    "This would drop observations that have been flagged")
                                        
                    




     #Column 2
     ##########################
     with col2:

          if sel_df != "":
            st.markdown("Selected Dataset")             
            st.dataframe(master_data)            

# When No data has been inported
else:
     st.markdown("Go to the import page to import your dataset(s)")

