from io import BytesIO

from PIL import Image, ImageEnhance, ImageFilter
import pytesseract


def preprocess_image(image: Image.Image) -> Image.Image:
    """
    Basic image preprocessing to improve OCR accuracy.
    """

    image = image.convert("L")

    # Increase contrast
    image = ImageEnhance.Contrast(image).enhance(1.5)

    # Slight sharpening
    image = image.filter(ImageFilter.SHARPEN)

    return image


def extract_text_from_image(file_bytes: bytes) -> str:
    """
    Extract text from an image using Tesseract OCR.
    """

    image = Image.open(BytesIO(file_bytes))

    processed_image = preprocess_image(image)

    text = pytesseract.image_to_string(
        processed_image,
        config="--psm 6"
    )

    return text.strip()