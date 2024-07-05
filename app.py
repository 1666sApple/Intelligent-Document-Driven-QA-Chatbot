import streamlit as st  # Streamlit for creating the web app
from PyPDF2 import PdfReader  # PyPDF2 for reading PDFs
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Langchain for splitting text
import os  # OS for handling environment variables
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # Langchain's Google Generative AI embeddings
import google.generativeai as genai  # Google Generative AI
from langchain.vectorstores import FAISS  # Langchain's FAISS vector store
from langchain_google_genai import ChatGoogleGenerativeAI  # Langchain's ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain  # Langchain's QA chain
from langchain.prompts import PromptTemplate  # Langchain's prompt template
from dotenv import load_dotenv  # Dotenv for loading environment variables from a .env file

# Load environment variables from a .env file
load_dotenv()

# Configure the Google Generative AI API with the provided API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_docs):
    """
    Extracts text from a list of uploaded PDF documents.

    Args:
        pdf_docs (list): List of uploaded PDF documents.

    Returns:
        str: Extracted text from all PDF documents.
    """
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    """
    Splits the extracted text into chunks of specified size with overlap.

    Args:
        text (str): The extracted text.

    Returns:
        list: List of text chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    text_chunks = text_splitter.split_text(text)
    return text_chunks

def get_vector_store(text_chunks):
    """
    Creates a vector store from the text chunks and saves it locally.

    Args:
        text_chunks (list): List of text chunks.

    Returns:
        FAISS: The FAISS vector store.
    """
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embeddings)
    vector_store.save_local("vectors/faiss")
    return vector_store

def get_conversational_chain():
    """
    Creates a conversational chain for Q&A using a prompt template and Google Generative AI model.

    Returns:
        load_qa_chain: The QA chain loaded with the specified model and prompt.
    """
    prompt_template = """
    Answer the questions as detailed as possible using the provided context. 
    Make sure to provide all the details. Remember not to provide any wrong answers.
    Context: \n{context}?\n\n
    Question: \n{question}\n
    Answer:
    """
    
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.5)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt, verbose=True)
    return chain

def user_input():
    """
    Handles user input for asking questions and displays the response.

    Uses the vector store to find relevant documents and the conversational chain to generate answers.
    """
    user_ques = st.text_input("Ask a question given the pdf you have uploaded below:")
    submit_button = st.button("Submit")
    
    if submit_button:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        new_db = FAISS.load_local("vectors/faiss", embeddings, allow_dangerous_deserialization=True)
        docs = new_db.similarity_search(user_ques, k=1)
        
        chain = get_conversational_chain()
        
        answer = chain(
            {"input_documents": docs, "question": user_ques},
            return_only_outputs=True,
        )
        
        print("Debug: Answer", answer)
        st.write("Response: ", answer["output_text"])

def main():
    """
    Main function to run the Streamlit app.

    Sets up the Streamlit app configuration, displays a header, and provides a sidebar menu for uploading PDFs.
    """
    st.set_page_config(page_title="PDF Q&A", page_icon="📚")
    st.header("Multiple PDFs Q&A Bot")
    
    # Sidebar menu for uploading PDFs
    with st.sidebar:
        st.title("Menu")
        pdf_docs = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
        if st.button("Upload PDFs"):
            if pdf_docs:
                text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(text)
                vector_store = get_vector_store(text_chunks)
                st.success("PDFs uploaded successfully")
            else:
                st.error("Please upload PDFs")
    
    user_input()

if __name__ == "__main__":
    main()
