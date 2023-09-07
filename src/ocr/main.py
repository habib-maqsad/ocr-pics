

from cgi import FieldStorage
from .mathpix import mathpix_ocr
from .tesseract import tesseract_ocr


def mathpix_request(
        buffer: FieldStorage,
        app_id: str,
        app_key: str,
        url: str):
    return mathpix_ocr(buffer, app_id, app_key, url)


def tesseract_request(buffer: FieldStorage) -> str:
    return tesseract_ocr(buffer)
