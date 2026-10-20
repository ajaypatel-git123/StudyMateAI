from text_chunker import split_text_into_chunks

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

chunks = split_text_into_chunks(
    text,
    chunk_size=10,
    overlap=2
)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}: {chunk}")