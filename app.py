# coding: utf-8

from flask import Flask
import logging

app = Flask(__name__)


logging.basicConfig(level=logging.INFO)


@app.route('/')
def index():
    return "Hello WeRun!"
