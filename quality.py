import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import info,describe,upload,Handle_Missing,Handle_Duplicates,Handle_outliers,Visualization,download,changeData,Rename_column
from ChatBot import chatbot_ui  # Import the chatbot function


st.set_page_config(
    page_title="Welcome To Data Quality Tool",
    page_icon="tool",
    layout="wide",
    
)





st.title("Welcome to Streamlit Data Quality")
    # Sidebar with buttons for different tasks
if "data" not in st.session_state:
     st.session_state.data = None
with st.sidebar:
    app=option_menu(
         menu_title='Data Quality Tool Options:',
         options=['Upload The Data','Info','Describe The Data','Change data type','Rename column','Handle Missing','Handle Duplicates','Handle outliers','Visualization','Download data','Chatbot'],
         icons=['upload','book','table','','','question-diamond','files','exclamation-circle','bar-chart','download','robot'],
         menu_icon='house',
         default_index=0,
         styles={
             "container": {"padding": "10!important","background-color":'#383b3e'},
              "icon": {"color": "#FF5733", "font-size": "18px"}, 
              
              "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#000080"},
               "nav-link-selected": {"background-color": "gold","color":"black",},}
            )
if app == "Upload The Data":
    upload.file_upload()     
if st.session_state.data is not None:
    if app == "Info":
        info.show_data_info(st.session_state.data)
         
    if app == "Describe The Data":
        describe.describe_data(st.session_state.data)
    if app == "Handle Missing":
        Handle_Missing.handle_missing_values(st.session_state.data) 
    if app == "Handle Duplicates":
        Handle_Duplicates.handle_duplicates(st.session_state.data)  
    if app == "Handle outliers":
        Handle_outliers.handle_outliers(st.session_state.data)  
    if app == "Download data":
        download.download_data(st.session_state.data)
    if app == "Visualization":
        Visualization.visualize(st.session_state.data)   
    #########################              
                
    if app == "Chatbot":
         chatbot_ui(st.session_state.data)  # Call the chatbot UI function
    if app=="Change data type":
        changeData.change(st.session_state.data)
    if app=="Rename column":
        Rename_column.rename_columns(st.session_state.data)
        

      

            
else:
    st.warning("Please upload a dataset first.")    
        
           
                
