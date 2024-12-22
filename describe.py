
import streamlit as st
import pandas as pd

def describe_data(data):
    st.markdown("## 📝 Data Description")
    st.dataframe(data.describe(include="all"))  
  






    
        