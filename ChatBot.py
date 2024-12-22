import streamlit as st
from langchain_ollama import ChatOllama
import upload 

def chatbot_ui(Data):
    """
    Displays the chatbot UI and handles interactions with the Ollama model.
    """
    st.title("🧠 Chat Application with Ollama and Langchain")

    # Form for user input
    with st.form("llm-form"):
        text = st.text_area("Enter your question or statement:")
        submit = st.form_submit_button("Submit")

    # Function to generate response
    def generate_response(input_text, uploaded_file):
        model = ChatOllama(model="llama3.2:1b", base_url="http://localhost:11434/")
        prompt = f"""
        Use the following  uploaded_file to answer the question:

        Dataset:
        { uploaded_file}

        Question:
        {input_text}
        """
        response = model.invoke(prompt)
        return response.content

    # Initialize chat history in session state
    if "chat_history" not in st.session_state:
        st.session_state['chat_history'] = []

    # Handle form submission
    if submit and text:
        with st.spinner("Generating response..."):
            response = generate_response(text, Data)
            st.session_state['chat_history'].append({"user": text, "ollama": response})
            st.write(response)

    # Display chat history
    st.write("## Chat History")
    for chat in reversed(st.session_state['chat_history']):
        st.write(f"**🧑 User**: {chat['user']}")
        st.write(f"**🧠 Assistant**: {chat['ollama']}")
        st.markdown("""
            <hr style="border: 3px solid tomato;">
                """, unsafe_allow_html=True)
