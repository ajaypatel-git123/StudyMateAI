from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

# 1. Load the pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 2. Create example sentences
sentences = [
    "Plants use sunlight to make their food.",
    "Photosynthesis helps plants produce food.",
    "The human heart pumps blood around the body."
]

# 3. Convert sentences into embeddings
embeddings = model.encode(sentences)

# 4. Display the shape of the embeddings
print("Embedding shape:", embeddings.shape)

# 5. Compare the first sentence with the other sentences
similarities = cos_sim(embeddings[0], embeddings[1:])

print("Similarity scores:")
print(similarities)