
import streamlit as st

def handle_missing_values(data):
    st.title("Handle Missing Values")
    
    missing_counts = data.isnull().sum()
    columns_with_missing = missing_counts[missing_counts > 0].index.tolist()

    if not columns_with_missing:
        st.success("No missing values found in the dataset!")
        return

    
    selected_column = st.selectbox("Select a column with missing values", columns_with_missing)

    
    method = st.selectbox(
        "Select a method to handle missing values",
        ["Fill with Mean", "Fill with Median", "Fill with Mode", "Drop Rows"]
    )

    
    st.write("### Dataset Preview (Before Handling)")
    st.dataframe(data[[selected_column]].head(10))  
    try:
         if st.button("Apply"):
             if method == "Fill with Mean":
                 data[selected_column].fillna(data[selected_column].mean(), inplace=True)
                 st.success(f"Missing values in '{selected_column}' filled with mean.")
             elif method == "Fill with Median":
                 data[selected_column].fillna(data[selected_column].median(), inplace=True)
                 st.success(f"Missing values in '{selected_column}' filled with median.")
             elif method == "Fill with Mode":
                 data[selected_column].fillna(data[selected_column].mode()[0], inplace=True)
                 st.success(f"Missing values in '{selected_column}' filled with mode.")
             elif method == "Drop Rows":
                 data.dropna(subset=[selected_column], inplace=True)
                 st.success(f"Rows with missing values in '{selected_column}' dropped.")
    except:
        st.error("This Method  does't the right  to handle  the missing ")           

        # Show the dataset preview after handling
    st.write("### Dataset Preview (After Handling)")
    st.dataframe(data[[selected_column]].head(10))
