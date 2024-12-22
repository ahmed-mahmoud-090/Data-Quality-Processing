import numpy as np
import pandas as pd
import streamlit as st
import io

def download_data(data):
    # Convert the DataFrame to CSV
    csv = data.to_csv(index=False)
    
    # Style the download section with custom markdown
    st.markdown(
        """
        <style>
            .download-btn {
                background-color: #4CAF50; 
                color: white; 
                font-size: 16px; 
                padding: 10px 20px; 
                border-radius: 5px; 
                cursor: pointer; 
            }
            .download-btn:hover {
                background-color: tomatto;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Informational text for the user
    st.markdown("""
        ### Download the Cleaned Dataset
        Click the button below to download the cleaned data as a CSV file. This will allow you to save and use the data for further analysis.
    """, unsafe_allow_html=True)
    
    # Display the download button with custom styling
    st.download_button(
        label="Download Dataset as CSV", 
        data=csv, 
        file_name='DataSetAfterCleaning.csv', 
        mime="text/csv", 
        key="download_button", 
        help="Click to download the cleaned dataset as a CSV file.",
        use_container_width=True
    )
