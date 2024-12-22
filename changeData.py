import streamlit as st
import pandas as pd

def change(data):
    if data is not None:
        st.write("Select a column and change its data type:")

        # Let the user select the column
        col = st.selectbox("Select Column:", options=data.columns)

        # Let the user select the new data type
        new_type = st.selectbox(
            f"Change Data Type for '{col}':",
            ["No Change", "int", "float", "str", "Date Time"],
            key=f"{col}_dtype"
        )

        # Attempt to change the data type
        try:
            if new_type == "int":
                # Handle non-numeric values by replacing them with NaN
                data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0).astype(int)
                st.success(f"Data Type Changed to {new_type} for '{col}'.")

            elif new_type == "float":
                # Handle non-numeric values by replacing them with NaN
                data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0.0).astype(float)
                st.success(f"Data Type Changed to {new_type} for '{col}'.")

            elif new_type == "str":
                # Convert to string directly
                data[col] = data[col].astype(str)
                st.success(f"Data Type Changed to {new_type} for '{col}'.")

            elif new_type == "Date Time":
                # Convert to datetime and handle invalid dates
                data[col] = pd.to_datetime(data[col], errors='coerce')
                st.success(f"Data Type Changed to {new_type} for '{col}'.")
                st.write("{data[col].dtype}")

        except Exception as e:
            st.error(f"Error: Unable to change data type for '{col}'. {str(e)}")
           
        st.write("---")
       
       
    else:
        st.error("No data available to change data type.")
