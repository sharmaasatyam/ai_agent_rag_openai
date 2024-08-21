import openai
import tiktoken

class QAService:
    def __init__(self, embedding_service):
        self.embedding_service = embedding_service

    def answer_question(self, question):
        try:
            answers = ""
            text_chunk = []
            # retrieving the relavent text according to the question
            relevant_texts = self.embedding_service.get_relevant_text(question)
            if not relevant_texts:
                return "Data Not Available",0
            #concatenating all the similarity result in one variable
            text_chunks = [text_chunk for text_chunk, similarity in relevant_texts]
            # provide the model name
            model_name = "gpt-4o-mini" 
            #crafting final prompt
            prompt = f"You are an expert in answering questions based on context.Your task is to answer questions based only on provided context.\n\nQuestion: {question}\n\nContext: {text_chunks}\n\nAnswer:"
            # calculating the count of token passed to openAI
            tokenizer = tiktoken.get_encoding("cl100k_base")
            tokens = tokenizer.encode(prompt)
            token_count = len(tokens)
            response = openai.ChatCompletion.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000
            )
            answers = response.choices[0].message['content'].strip()
            return answers if answers else "Data Not Available", token_count
        except Exception as e:
            print(f"Error generating answer: {e}")
            return "An error occurred while generating the answer. Please try again later."
