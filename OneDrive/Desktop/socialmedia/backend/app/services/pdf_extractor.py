import fitz


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extract text from a PDF while preserving basic
    paragraph and page structure.
    """

    document = fitz.open(stream=file_bytes, filetype="pdf")

    pages = []

    try:
        for page_number, page in enumerate(document, start=1):
            text = page.get_text("text")

            if text.strip():
                pages.append(
                    f"--- Page {page_number} ---\n{text.strip()}"
                )

        return "\n\n".join(pages)

    finally:
        document.close()