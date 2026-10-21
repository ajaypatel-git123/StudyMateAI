from pdf_reader import extract_text_from_pdf
from text_chunker import split_text_into_chunks

pages = extract_text_from_pdf("50 ques.pdf")

chunks = split_text_into_chunks(
  pages,
  chunk_size= 500,
  overlap=50
  )

# Step 3: Display the results
print("Total pages:", len(pages))
print("Total chunks:", len(chunks))

if chunks:
    print("\nFirst chunk page:", chunks[0]["page_number"])
    print("First chunk text:\n", chunks[0]["text"])
else:
    print("No text found in the PDF.")  


from sentence_transformers import SentenceTransformer

# load the embedding model

model = SentenceTransformer("all-MiniLM-L6-v2")

chunk_texts = [chunk["text"] for chunk in chunks]


chunk_embeddings = model.encode(
   chunk_texts,
   convert_to_tensor=True,
   show_progress_bar=True
)

print("\nEmbeddings shape:",chunk_embeddings.shape)

from sentence_transformers.util import cos_sim

question = input("\n Ask a question about the pdf")

query_embeddings = model.encode(
    question,
    convert_to_tensor=True
)

scores = cos_sim(query_embeddings,chunk_embeddings )[0]

top_k = min(3 , len(chunks))
top_results = scores.topk(k = top_k)

print("\nMost relevant passages:")

for score, index in zip(top_results.values, top_results.indices):
    chunk = chunks[index.item()]

    print("\nPage:", chunk["page_number"])
    print("Similarity:", round(score.item(), 4))
    print("Text:", chunk["text"])