
# AI Agent with Retrieval-Augmented Generation (RAG)

## Overview

This project implements an AI agent that leverages Retrieval-Augmented Generation (RAG) to answer questions based on the content of a large PDF document. The agent uses the `gpt-4o-mini` model from OpenAI to generate responses and posts results to Slack. It employs a custom embedding service for text chunking and embedding, and a QA service for question answering.

## Features

- Extracts text from PDF documents.
- Chunks and embeds text using OpenAI's `gpt-4o-mini` model.
- Answers user questions based on the extracted and embedded text.
- Posts the answers to a Slack channel.
- Handles errors gracefully and logs issues.

## Prerequisites

Before running the service, ensure you have the following:

- **Python 3.7+**: Make sure you have Python installed on your machine.
- **OpenAI API Key**: Obtain an API key from [OpenAI](https://platform.openai.com/signup).
- **Slack Token**: Create a Slack app and obtain a token from [Slack API](https://api.slack.com/apps).

## Project Structure

- `main.py`: Entry point for running the application.
- `config.py`: Configuration file for API keys and settings.
- `embedding_service.py`: Handles text extraction, chunking, and embedding.
- `qa_service.py`: Handles question answering using the embedded text.
- `slack_service.py`: Manages posting messages to Slack.
- `requirements.txt`: Lists the Python packages required for the project.
- `documents/`: Folder containing the PDF file.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ai_agent_rag_openai.git
   cd ai_agent_rag_openai
   ```

2. **Install Dependencies**

   Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Configuration**

   Create a `.env` file in the root directory of the project with the following content:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   SLACK_TOKEN=your_slack_token
   SLACK_CHANNEL=your_slack_channel
   ```

   Ensure you replace the placeholders with your actual API key, token, and Slack channel ID.

## Usage

1. **Prepare Your PDF Document**

   Place your PDF file in the `documents/` folder. Name the file appropriately (e.g., `company_handbook.pdf`).

2. **Modify `main.py` if Necessary**

   Update the file path and questions in `main.py` as needed.

3. **Run the Application**

   ```bash
   python main.py
   ```

   The application will extract text from the PDF, generate embeddings, answer the specified questions, and post the results to Slack.

## Error Handling

The application includes basic error handling for:
- **Text Extraction**: Errors in extracting text from the PDF will be logged.
- **Embedding Generation**: Issues with embedding text chunks will be logged.
- **Question Answering**: Errors during question answering will be handled, and a default message "Data Not Available" will be returned.
- **Slack Posting**: Issues posting messages to Slack will be logged.

## Testing

To test the application, you can:
1. Use sample PDFs and questions.
2. Check the logs for any errors during execution.

## Contributing

Feel free to fork the repository and submit pull requests. Contributions to improve functionality, fix bugs, or enhance documentation are welcome.


## Contact

For any questions or support, please contact:

- **Email**: [satyamsharmaa15@gmail.com]
