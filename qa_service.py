class QAService:
    def __init__(self, embedding_service):
        self.embedding_service = embedding_service

    def answer_question(self, question):
        relevant_texts = self.embedding_service.get_relevant_text(question)
        answers = []
        for text in relevant_texts:
            response = openai.Completion.create(
                model="gpt-4o-mini",
                prompt=f"Question: {question}\n\nContext: {text}\n\nAnswer:",
                max_tokens=100
            )
            answers.append(response.choices[0].text.strip())
        return answers[0] if answers else "Data Not Available"
