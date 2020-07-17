from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'key-1234'

@app.route('/')
def home():
    return render_template('form.html', prompts=story.prompts)