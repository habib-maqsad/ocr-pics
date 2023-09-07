
from cgi import FieldStorage
from pytesseract import image_to_string, Output
from PIL import Image


def tesseract_ocr(buffer: FieldStorage):
    try:
        image = Image.open(buffer)
        expression = image_to_string(
            image, lang='eng', output_type=Output.DICT)
        text = expression['text']

        print("PARSED TEXT: ", text)

        return text

    except Exception as e:
        return 'Error: Could not parse image...'
