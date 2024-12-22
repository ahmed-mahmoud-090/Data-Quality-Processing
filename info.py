import streamlit as st
import pandas as pd

# Function to display the dataset and column information in styled cards
def show_data_info(data):
    # Custom CSS styles
    st.markdown("""
    <style>
        .header {
            font-size: 24px;
            font-weight: bold;
            color: #4CAF50;
            margin-bottom: 10px;
        }
        .subheader {
            font-size: 18px;
            color: #333;
            margin-bottom: 10px;
        }
        .column-info {
            font-size: 16px;
            color: #555;
        }
        .unique-values {
            font-size: 14px;
            color: #1f77b4;
        }
        .success-message {
            font-size: 16px;
            color: #28a745;
        }
        .error-message {
            font-size: 16px;
            color: #dc3545;
        }
        .card {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .card-header {
            font-size: 18px;
            font-weight: bold;
            color: #007BFF;
            margin-bottom: 10px;
        }
        .card-body {
            font-size: 14px;
            color: #333;
        }
    </style>
    """, unsafe_allow_html=True)

    # Display basic dataset info
    st.markdown('<p class="header">Dataset Information</p>', unsafe_allow_html=True)
    st.write(f"Number of Rows: {data.shape[0]}")
    st.write(f"Number of Columns: {data.shape[1]}") 

    st.markdown('<p class="header">Column Information</p>', unsafe_allow_html=True)

    special_chars_dict = {}

    # Iterate over each column and display its details inside cards
    for col in data.columns:
        with st.container():
            st.markdown(f'<div class="card">', unsafe_allow_html=True)
            st.markdown(f'<div class="card-header">Column: {col}</div>', unsafe_allow_html=True)
            
            st.markdown(f'<div class="card-body">', unsafe_allow_html=True)
            
            # Display data type
            st.write(f"<p class='column-info'>Data Type: {data[col].dtype}</p>", unsafe_allow_html=True)

            # Count of numerical values
            num_values = data[col].apply(pd.to_numeric, errors='coerce').notnull().sum()
            st.write(f"<p class='column-info'>Number of Numerical Values: {num_values}</p>", unsafe_allow_html=True)

            # Count of NaN values
            nan_values = data[col].isnull().sum()
            st.write(f"<p class='column-info'>Number of NaN Values: {nan_values}</p>", unsafe_allow_html=True)

            # Count of unique values
            unique_values = data[col].nunique()
            st.write(f"<p class='column-info'>Count of Unique Values: {unique_values}</p>", unsafe_allow_html=True)

            # Count special characters in the column
            special_chars = get_special_char_count(data[col], special_chars_dict)
            st.write(f"<p class='column-info'>Count of Special Characters: {special_chars}</p>", unsafe_allow_html=True)

            # Display unique values if there are fewer than 20 unique values
            if unique_values < 20:
                st.write(f"<p class='unique-values'>Unique Values: {data[col].unique()}</p>", unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

     # Adds a line break between cards for better readability
        st.markdown("""
            <hr style="border: 3px solid tomato;">
                """, unsafe_allow_html=True)
 

      
# Function to count special characters in a column
def get_special_char_count(column, special_chars_dict):
    if column.dtype == "object":
        special_chars = [char for char in column.unique() if not str(char).isalnum()]
        special_chars_dict[column.name] = special_chars
        return len(special_chars)
    return 0

# Example usage
# data = pd.read_csv('your_dataset.csv')
# show_data_info(data)


