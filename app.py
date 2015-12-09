# coding: utf-8

from flask import Flask, render_template
import logging

app = Flask(__name__)


logging.basicConfig(level=logging.INFO)


@app.route('/')
def index():
    return render_template('index.html')
