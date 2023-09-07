

from cgi import FieldStorage
from .mathpix import math_pix_request
from .tesseract import tesseract_request


def ocr_request(buffer: FieldStorage, type: str) -> str:
    if type == 'mathpix':
        return math_pix_request(buffer)
    elif type == 'tesseract':
        return tesseract_request(buffer)
    else:
        raise Exception('Unknown OCR type')


def mathpix_request(
        buffer: FieldStorage,
        app_id: str,
        app_key: str,
        url: str):
    return math_pix_request(buffer, app_id, app_key, url)


def tesseract_request(buffer: FieldStorage) -> str:
    return tesseract_request(buffer)
