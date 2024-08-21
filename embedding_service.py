import openai
import numpy as np
from scipy.spatial.distance import cosine

class EmbeddingService:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.embeddings = []
        self.text_chunks = []

    def embed_text(self, text_chunks):
        for chunk in text_chunks:
            try:
                response = openai.Embedding.create(
                    model="text-embedding-3-large",  # The model name for generating embeddings
                    input=chunk
                )
                embedding = response['data'][0]['embedding']
                self.embeddings.append(embedding)
                self.text_chunks.append(chunk)
            except Exception as e:
                print("Error:", e)
                raise RuntimeError("Failed to embed text chunk. Please try again later.")

    def get_relevant_text(self, question, top_k=30):
        try:
            # Generate embedding for the question
            question_embed_response = openai.Embedding.create(
                model="text-embedding-3-large",
                input=question
            )
            question_embedding = question_embed_response['data'][0]['embedding']
            
            # Calculate cosine similarities
            similarities = [1 - cosine(question_embedding, emb) for emb in self.embeddings]
            
            # Get top_k indices with highest similarity
            top_indices = np.argsort(similarities)[-top_k:]
            
            return [self.text_chunks[i] for i in top_indices]
        except Exception as e:
            print("Error:", e)
            raise RuntimeError("Failed to retrieve relevant text. Please try again later.")
