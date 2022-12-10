import streamlit as st
import numpy as np
from PIL import Image

# PAGE CONFIGURATION
favicon = Image.open("favicon.png")
favicon2array = np.array(favicon)
st.set_page_config("LAIA - DPPT", favicon2array, "wide", "auto", {"Get help": None, "Report a Bug": None, "About": None})
  
# HOME SCREEN
st.title("DATA PRE PROCESSING TOOL")
st.text("The simplest tool for detection, viewing and manipulating outliers.")
       
with st.expander("See functionalities"):
    st.write("""
        1. See the information about the uploaded file.
        2. See the basic information about the attributes.
        3. Option to visualize a histogram of every attribute.
        4. Option to detect and visualize outliers.
        5. Option to select a method for change the outliers.
        6. Option to download file with modifications.
        7. Option to compare before and after attributes information .
    """)

st.markdown("Read the documentation in [here](https://github.com/laiauft)!")
st.markdown("Go to the **Dashboard** page to begin.")