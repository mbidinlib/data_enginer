
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

#Installed programs
#pip install streamlit-multipage


#Add background color
st.markdown(
    '''<style>
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
        color: #DC7633;
        font-family: oopen sans;
    }
    p {
        font-family: open sans;
    }    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
<body style="background-color:#1c87c9;">
</body>

''', unsafe_allow_html=True)


#st.sidebar.markdown("# Home page")
with st.sidebar.container():
    st.image('picture.jpg',
    caption='Mathew Bidinlib', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    #st.image(image, width= use_column_width=True)

st.markdown("# MGlory Data Engineering Toolkit ")
st.markdown("""
    Welcome to MGlory Data Engineering toolkit.
    This is a python based tool that would help you prepare your dataset for analysis.
    The tool contains the following components:
    - **Data Import**
    With the data import page, you would be able to import upto five (5) datasets for your work.
    Each dataset is in a seperate tab and you can navigate across tabs
    - **Check Duplicates**
    You can check if your data has duplicates using some key variables 
    and also remove duplicates if there are any
    - **Check Outliers**
    You can check if some variables have outliers given a certain multiplier effect
    - **Merge Data**
    This would help you to merge selected datasets that you imported into one. 
    You may also append datasets if needed
    """)

def footer(st):
    st.write("Developed by [Mathew Bidinlib](https://github.com/mbidinlib/)")


def header(st):
    st.write("This app is free to use")




#********************
# Manage Session State
# *********************
import streamlit.ReportThread as ReportThread
from streamlit.server.Server import Server

def get_session():
    ctx = ReportThread.get_report_ctx().session_id
    this_session = None
    current_session = Server.get_current()._get_session_info(ctx)
    this_session = current_session.session
    # st.write("ch",current_session.session)

    if current_session is None:
        raise RuntimeError(
            "Oh noes. Couldn't get your Streamlit Session object"
            'Are you doing something fancy with threads?')

    return this_session

def get_state(hash_funcs=None):
    session = get_session()
    if not hasattr(session, "_custom_session_state"):
        session._custom_session_state = SessionState(session, hash_funcs)

    return session._custom_session_state

class SessionState:

    def __init__(self, session, hash_funcs):
        """Initialize SessionState instance."""
        self.__dict__["_state"] = {
            "data": {},
            "hash": None,
            "is_rerun": False,
            "session": session,
        }

    def __call__(self, **kwargs):
        """Initialize state data once."""
        for item, value in kwargs.items():
            if item not in self._state["data"]:
                self._state["data"][item] = value

    def __getitem__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)

    def __getattr__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)

    def __setitem__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value

    def __setattr__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value

    def clear(self):
        """Clear session state and request a rerun."""
        self._state["data"].clear()
        self._state["session"].request_rerun()

    def sync(self):
        """Rerun the app with all state values up to date from the beginning to fix rollbacks."""

        # Ensure to rerun only once to avoid infinite loops
        # caused by a constantly changing state value at each run.
        #
        # Example: state.value += 1
        if self._state["is_rerun"]:
            self._state["is_rerun"] = False

        elif self._state["hash"] is not None:
            if self._state["hash"] != self._state["hasher"].to_bytes(self._state["data"], None):
                self._state["is_rerun"] = True
                self._state["session"].request_rerun()

        self._state["hash"] = self._state["hasher"].to_bytes(self._state["data"], None)


 