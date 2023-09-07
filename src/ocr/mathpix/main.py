
from cgi import FieldStorage
import requests
import os
import json


def mathpix_api(buffer: FieldStorage, MATH_PIX_APP_ID: str, MATHPIX_APP_KEY: str, MATH_PIX_URL: str):

    response = requests.post(MATH_PIX_URL,
                             files={"file": buffer},
                             data={
                                 "options_json": json.dumps({
                                     "math_inline_delimiters": ["$", "$"],
                                     "rm_spaces": True
                                 })
                             },
                             headers={
                                 "app_id": MATH_PIX_APP_ID,
                                 "app_key": MATHPIX_APP_KEY
                             }
                             )

    return response


def mathpix_ocr(buffer: FieldStorage,  app_id: str, app_key: str, url: str):
    response = mathpix_api(buffer, app_id, app_key, url)
    data = (json.dumps(response.json(), indent=4, sort_keys=True))
    text = json.loads(data)['text']
    print("PARSED TEXT (MATHPIX): ", text)
    return text
