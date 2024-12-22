import streamlit as st

def rename_columns(data):
    """
    Allows users to rename columns in the dataset.
    """
    if data is not None:
        st.write("### Rename Columns in the Dataset")
        
        # Let the user select a column to rename
        col_to_rename = st.selectbox("Select a column to rename:", options=data.columns)

        # Let the user input the new name
        new_col_name = st.text_input("Enter the new column name:", key=f"rename_{col_to_rename}")

        # Rename the column when the user confirms
        if st.button("Rename Column"):
            if new_col_name.strip() == "":
                st.warning("Column name cannot be empty.")
            elif new_col_name in data.columns:
                st.warning("Column name already exists. Choose a unique name.")
            else:
                data.rename(columns={col_to_rename: new_col_name}, inplace=True)
                st.success(f"Column '{col_to_rename}' has been renamed to '{new_col_name}'.")

        # Display the updated dataframe
        st.write("### Updated Dataset")
        st.dataframe(data)
    else:
        st.error("No dataset found. Please upload a dataset first.")
