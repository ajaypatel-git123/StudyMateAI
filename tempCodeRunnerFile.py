from pdf_reader import extract_text_from_pdf
from text_chunker import split_text_into_chunks

# Step 1: Extract pages from PDF
pages = extract_text_from_pdf("check.pdf")

# Step 2: Create chunks with page numbers
chunks = split_text_into_chunks(
    pages,
    chunk_size=500,
    overlap=50
)

# Step 3: Display results
print("PDF extracted successfully!")
print("Total pages:", len(pages))
print("Total chunks:", len(chunks))

if chunks:
    print("\nFirst chunk:")
    print("Page number:", chunks[0]["page_number"])
    print("Text:\n", chunks[0]["text"])
else:
    print("No text found in PDF.")