from flask import Flask, abort, jsonify, make_response, request
import os
from flask_cors import cross_origin
import requests
from http import HTTPStatus

from src.ocr.main import ocr_request


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, world!'


@app.route('/hello')
def ok():
    return 'Hello, flasking world!'


@app.post('/tesseract-ocr')
@cross_origin()
def tesseract_ocr():
    image = request.files.get('image')

    if image is None:
        response = jsonify({'error': 'Image not provided...'})
        response.status_code = HTTPStatus.BAD_REQUEST
        return abort(make_response(response))

    return ocr_request(image, 'tesseract')


# app.run(host='localhost', port=8080, debug=True)
