import pytesseract
from PIL import Image

# Configure tesseract executable path if necessary
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR/tesseract'

def extract_text_from_image(image_path):
    """
    Extract text from an image using Tesseract OCR.
    :param image_path: Path to the image file
    :return: Extracted text as a string
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text