import os
from config import Config
from pdf_processor import extract_text_from_pdf, chunk_text
from embedding_service import EmbeddingService
from qa_service import QAService
from slack_service import SlackService

def main(pdf_path, questions):
    # Extract and chunk the text from PDF
    text = extract_text_from_pdf(pdf_path)
    text_chunks = chunk_text(text)

    # Initialize embedding services
    embedding_service = EmbeddingService(api_key=Config.OPENAI_API_KEY)
    embedding_service.embed_text(text_chunks)

    qa_service = QAService(embedding_service)
    #slack_service = SlackService(slack_token=Config.SLACK_TOKEN)

    # Answer questions and post results to Slack
    for question in questions:
        answer,token_count = qa_service.answer_question(question)
        message = f"Question: {question}\nAnswer: {answer} \n\nToken_Used: {token_count}"
        print(message)
        #slack_service.post_message(Config.SLACK_CHANNEL, message)

if __name__ == "__main__":
    pdf_folder = "pdf"
    pdf_filename = "handbook.pdf"  # Replace with your file name according to your requirement
    pdf_path = os.path.join(pdf_folder, pdf_filename)
    #pdf_path = "path_to_your_pdf.pdf"
    questions = [
        "What is the name of the company?",
        "Who is the CEO of the company?",
        "What is their vacation policy?",
        "What is the termination policy?"
    ]
    main(pdf_path, questions)
