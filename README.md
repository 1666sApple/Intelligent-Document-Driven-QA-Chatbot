# Intelligent Document-Driven QA Chatbot

Welcome to the Intelligent Document-Driven QA Chatbot repository. This project allows users to upload PDF documents and ask questions based on the content of those documents. The chatbot uses Google Generative AI to understand and answer the questions accurately.

## Repository Link

[GitHub Repository](https://github.com/1666sApple/Intelligent-Document-Driven-QA-Chatbot)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Intelligent Document-Driven QA Chatbot is built using Streamlit for the web interface and integrates various AI components from Langchain and Google Generative AI. The application allows users to upload multiple PDF documents, extracts the text from these documents, processes the text into manageable chunks, and uses a conversational AI model to answer user questions based on the content of the uploaded PDFs.

## Features

- Upload multiple PDF documents
- Extract and process text from PDFs
- Create a vector store from the text chunks
- Perform similarity search to find relevant text chunks
- Use Google Generative AI for question answering
- Interactive and user-friendly web interface

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/1666sApple/Intelligent-Document-Driven-QA-Chatbot.git
    cd Intelligent-Document-Driven-QA-Chatbot
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the project root.
    - Add your Google API key to the `.env` file:
        ```env
        GOOGLE_API_KEY=your_api_key_here
        ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Use the sidebar to upload PDF documents.

4. Ask questions based on the content of the uploaded PDFs and get accurate answers from the chatbot.

## Contributing

We welcome contributions to the Intelligent Document-Driven QA Chatbot project. If you have any suggestions, bug reports, or feature requests, please create an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Make your changes.
4. Commit your changes:
    ```bash
    git commit -m 'Add some feature'
    ```
5. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

