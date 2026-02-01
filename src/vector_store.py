
class EndeeVectorStore:
    """
    Abstraction layer over Endee vector database.
    """

    def __init__(self):
        self.vectors = []
        self.metadata = []

    def add_vectors(self, vectors, metadata):
        self.vectors.extend(vectors)
        self.metadata.extend(metadata)

    def search(self, query_vector, top_k=3):
        import numpy as np

        scores = []
        for i, vec in enumerate(self.vectors):
            score = np.dot(query_vector, vec) / (
                np.linalg.norm(query_vector) * np.linalg.norm(vec)
            )
            scores.append((score, self.metadata[i]))

        scores.sort(reverse=True, key=lambda x: x[0])
        return scores[:top_k]
