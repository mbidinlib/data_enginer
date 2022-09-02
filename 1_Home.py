
'''
Date: Wed Aug 23 21:12:18 2022
@author: Glooory
Purpose: Data Engineering
'''
from io import StringIO
import pandas as pd
import streamlit as st

# Set page outline
st. set_page_config(layout="wide")
#st.set_page_config(page_title="MGlory Data-Engineering", page_icon="📊")
#Installed programs
#pip install streamlit-multipage

#Add background color
body_format = '''
<style>
    body {
        background-color: brown;
        secondary-background-color:red;
        }
    h1 {
        color: maroon;
        font-family: Tahoma;
        font-size: 200%;
    }
    h2 {
        color: #BA4A00;
        font-family: open sans;
    }
    h3 {
        color: #045106;
        font-family: oopen sans;
    }
    p {
        font-family: open sans;
    }    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    '''
st.markdown(body_format, unsafe_allow_html=True)


#st.sidebar.markdown("# Home page")
#with st.sidebar.container():
#    sbcol1, sbcol2, = st.columns(2)
#    
#    sbcol1.image('picture.jpg',
#    caption='Mathew Bidinlib', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
#    #st.image(image, width= use_column_width=True)

st.markdown("# MGlory Data Engineering Toolkit ")

st.markdown("""
    Welcome to MGlory Data Engineering toolkit.
    This is a python based tool that would help you prepare your dataset for analysis.
    The tool contains the following components""")

hcol1, hcol2 = st.columns(2)

with hcol1:
    st.markdown("<h4><u>Import Page</u></h4>",unsafe_allow_html=True)
    exp1 = st.expander("Help note",expanded=False)
    exp1.write('''
    This page is the starting point where you would be able to import up to five (5) datasets for your work.
    There is a tab dedicated for each dataset and you can navigate across tabs
    ''')
with hcol2:
    st.markdown("<h4><u>Duplicates Page</u></h4>",unsafe_allow_html=True)
    exp2 = st.expander("Help note",expanded=False)
    exp2.write('''
    This page would help you check for duplicates in the imported datasets using some key variables. 
    You would also be able to download duplicate reports and remove duplicates.
    ''')
with hcol1:
    st.markdown("<h4><u>Outliers Page</u></h4>",unsafe_allow_html=True)
    exp3 = st.expander("Help note",expanded=False)
    exp3.write('''
    This page is would help you check for outliers in your importd dataset
    ''')

with hcol2:
    st.markdown("<h4><u>Merge Page</u></h4>",unsafe_allow_html=True)
    exp4 = st.expander("Help note",expanded=False)
    exp4.write('''
    This would help you to merge selected datasets that you imported. 
    You may also append datasets if needed.
    ''')


# Set the footer
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.github.com/mbidinlib/" target="_blank">Mathew Bidinlib </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
