import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
        title="Srinidhi Kuchana",
        url=os.getenv("URL"),
        about="B.Tech CSE student at MRECW (2024–2028), passionate about AI/ML, derivative markets, and competitive programming. Currently a Meta Production Engineering Fellow at MLH."
    )