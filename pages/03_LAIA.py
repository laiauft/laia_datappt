import streamlit as st
import numpy as np
from PIL import Image

# PAGE CONFIGURATION
favicon = Image.open("favicon.png")
favicon2array = np.array(favicon)
st.set_page_config("LAIA", favicon2array, "wide", "auto", {"Get help": None, "Report a Bug": None, "About": None})

st.write("SOON!")