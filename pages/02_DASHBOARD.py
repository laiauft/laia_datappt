import streamlit as st
import numpy as np
from PIL import Image
from functions import *

# PAGE CONFIGURATION
favicon = Image.open("favicon.png")
favicon2array = np.array(favicon)
st.set_page_config("Dashboard - DPPT", favicon2array, "wide", "auto", {"Get help": None, "Report a Bug": None, "About": None})

# DASHBOARD SCREEN
st.title("DASHBOARD")
st.text("Upload a csv file to begin!")

uploaded_file = st.file_uploader("Choose a .csv file", type=['csv'], accept_multiple_files=False)

if uploaded_file is not None:
        dataframe = convert_to_dataframe(uploaded_file)
        file_information = get_file_information(uploaded_file, dataframe)
        all_attributes_basic_information = get_all_attributes_basic_information(dataframe)
        list_of_attributes = file_information[3]
        
        with st.expander("View information about file"):
                st.write("      - **File name:** ", file_information[0])
                st.write("      - **Number of attributes:** ", file_information[1])
                st.write("      - **Instances:** ", file_information[2])
                st.write("      - **List of attributes:**")     
                st.write(list_of_attributes)

        with st.expander("Display basic information about the attributes"):
                st.dataframe(all_attributes_basic_information)

        with st.expander("Display all dataframe"):
                st.dataframe(dataframe)

        with st.expander("Display the attributes line chart"):
                selected_attribute = st.selectbox(
                        'Select the attribute',
                        (list_of_attributes),
                        key = 'sb_one',
                )
                attribute_position = list_of_attributes.index(selected_attribute)
                st.line_chart(dataframe.get(list_of_attributes[attribute_position]))
                
        with st.expander("Display the option to detect outliers"):
                selected_attribute_out = st.selectbox(
                        'Select the attribute',
                        (list_of_attributes),
                        key = 'sb_two',
                )
                attribute_position = list_of_attributes.index(selected_attribute_out)       
                       
                std_value = dataframe[selected_attribute_out].std()
                has_outliers = outliers_verification_method_one(std_value)      
                st.subheader("Detecting outliers with method one")
                st.caption("---> Using predetermined standard deviation (10)")
                st.write(f"Standard deviation for {selected_attribute_out}: ", std_value)
                st.write(selected_attribute_out, 'has outliers? ', has_outliers)
                
                st.subheader("Detecting outliers with method two")
                st.caption("---> Using median plus four standard deviation")
                
                outliers = outliers_verification_method_two(dataframe, selected_attribute_out)
                st.write("Median with four default deviation: ", outliers[0])
                st.write("Median without four default deviation: ", outliers[1])
                st.write(f"Numbers of outliers in {selected_attribute_out}: ", len(outliers[2]))
                st.write(f"Outliers in {selected_attribute_out}:")
                st.write(outliers[2])
                
