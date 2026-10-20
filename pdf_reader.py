import pymupdf
import easyocr

# Load OCR only when a scanned page needs it.
# Reuse the same reader across all pages in this Python process.
reader = None


def get_ocr_reader():
    global reader

    if reader is None:
        print("Loading EasyOCR model... Please wait.")
        reader = easyocr.Reader(["en", "hi"], gpu=False)
        print("EasyOCR ready!")

    return reader


def extract_text_from_pdf(pdf_path):
    pages = []

    with pymupdf.open(pdf_path) as document:
        for page_number, page in enumerate(document, start=1):
            text = page.get_text().strip()

            # Use OCR only if selectable text is missing.
            if not text:
                print(f"Running OCR on page {page_number}...")

                pix = page.get_pixmap(dpi=200)
                image_bytes = pix.tobytes("png")

                ocr_reader = get_ocr_reader()
                results = ocr_reader.readtext(image_bytes)

                text = "\n".join(
                    result[1] for result in results
                ).strip()

            pages.append({
                "page_number": page_number,
                "text": text
            })

    return pages