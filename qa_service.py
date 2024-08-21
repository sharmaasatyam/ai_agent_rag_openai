import openai
import tiktoken

class QAService:
    def __init__(self, embedding_service):
        self.embedding_service = embedding_service

    def answer_question(self, question):
        try:
            relevant_texts = self.embedding_service.get_relevant_text(question)
            if not relevant_texts:
                return "Data Not Available"
            
            # provide the model name
            model_name = "gpt-4o-mini" 

            answers = []
            for text in relevant_texts:
                prompt = f"You are an expert in answering questions based on context.Your task is to answer questions based only on provided context.\n\nQuestion: {question}\n\nContext: {text}\n\nAnswer:"
                # Getting the count of token passed to openAI
                tokenizer = tiktoken.get_encoding("cl100k_base")
                tokens = tokenizer.encode(prompt)
                token_count = len(tokens)
                response = openai.ChatCompletion.create(
                    model=model_name,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=1000
                )
                answers.append(response.choices[0].message['content'].strip())
            
            return answers[0] if answers else "Data Not Available", token_count
        except Exception as e:
            print(f"Error generating answer: {e}")
            return "An error occurred while generating the answer. Please try again later."
