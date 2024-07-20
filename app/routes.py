from flask import render_template
from app import app
import datetime
from googleapiclient.discovery import build

@app.route('/')
def index():
    return render_template('index.html')
