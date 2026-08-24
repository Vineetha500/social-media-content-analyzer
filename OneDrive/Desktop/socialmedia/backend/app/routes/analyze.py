from fastapi import APIRouter, UploadFile, File, HTTPException

from app.schemas.analysis import AnalysisResponse
from app.services.pdf_extractor import extract_text_from_pdf
from app.services.ocr_service import extract_text_from_image
from app.services.analyzer import analyze_text


router = APIRouter(
    prefix="/api",
    tags=["Analysis"]
)


ALLOWED_EXTENSIONS = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
}

MAX_FILE_SIZE = 10 * 1024 * 1024


@router.post(
    "/analyze",
    response_model=AnalysisResponse
)
async def analyze_document(
    file: UploadFile = File(...)
):

    filename = file.filename or ""

    extension = ""

    if "." in filename:
        extension = "." + filename.rsplit(".", 1)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=(
                "Unsupported file type. "
                "Please upload PDF, PNG, JPG or JPEG."
            )
        )

    file_bytes = await file.read()

    if not file_bytes:
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is empty."
        )

    if len(file_bytes) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size must be less than 10 MB."
        )

    try:

        if extension == ".pdf":

            extracted_text = extract_text_from_pdf(
                file_bytes
            )

            file_type = "PDF"

        else:

            extracted_text = extract_text_from_image(
                file_bytes
            )

            file_type = "Image / OCR"

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Text extraction failed: {str(error)}"
        )

    if not extracted_text.strip():

        raise HTTPException(
            status_code=422,
            detail=(
                "No readable text was found in the document. "
                "For scanned PDFs, upload the scanned page as an image "
                "or use a PDF with an embedded text layer."
            )
        )

    analysis = analyze_text(
        extracted_text
    )

    return AnalysisResponse(
        filename=filename,
        file_type=file_type,
        extracted_text=extracted_text,
        **analysis
    )