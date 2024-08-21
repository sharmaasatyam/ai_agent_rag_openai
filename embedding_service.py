import openai
import numpy as np

class EmbeddingService:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.embeddings = []
        self.text_chunks = []

    def embed_text(self, text_chunks):
        for chunk in text_chunks:
            embedding = openai.embeddings(text=chunk)["data"][0]["embedding"]
            self.embeddings.append(embedding)
            self.text_chunks.append(chunk)

    def get_relevant_text(self, question, top_k=1):
        question_embedding = openai.embeddings(text=question)["data"][0]["embedding"]
        similarities = [np.dot(question_embedding, emb) for emb in self.embeddings]
        top_indices = np.argsort(similarities)[-top_k:]
        return [self.text_chunks[i] for i in top_indices]
