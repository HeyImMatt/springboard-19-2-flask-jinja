from flask import Flask, redirect, request, render_template, url_for
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story, Story

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'key-1234'

@app.route('/')
def home():
    return render_template('form.html', prompts=story.prompts)

@app.route('/story', methods=['GET', 'POST'])
def show_story():
    if request.method == 'POST':
        story_text = story.generate(request.form)
        return render_template('story.html', story_text=story_text)