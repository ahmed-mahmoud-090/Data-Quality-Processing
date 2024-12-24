# Data-Quality-Processing

#Streamlit Data Assistant with Chatbot
## **Overview** 
A Streamlit-powered web application that allows users to upload datasets (CSV, Excel), manipulate data types, and interact with a Language Model (LLM) to analyze and query data in a conversational format. The application enables data transformations such as changing data types, renaming columns, and running queries using the chatbot powered by LangChain.

## **Features**
- **Upload Dataset:** Allows users to upload CSV or Excel files.
- **Change Data Types:** Modify column data types (int, float, string, datetime).
- **Rename Columns:** Easily rename columns in the dataset.
- **Handle Duplicated Values:** Identify and handle duplicate data.
- **Handle Missing Values:** Detect and handle missing values.
- **Chatbot Interaction:** Interact with a language model to query the dataset and analyze data.
- **Persist Data:** All user interactions are saved and persisted across sessions using Streamlit’s session state.

## **Technologies Used**
- **Streamlit:** For creating the interactive web interface.
- **Pandas:** For data manipulation and handling.
- **LangChain:** To integrate and interact with language models.
- **Ollama:** For querying data with a local LLM.
- **Python:** Core programming language for backend functionality.

## **Acknowledgments**
We would like to thank the following:
- **Streamlit:** For providing the app framework.
- **LangChain:** For enabling the use of language models.
- **Ollama:** For the pre-trained language model powering the chatbot.

## **Steps to Run the App**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Data-Quality-Processing.git
