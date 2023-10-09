from flask import Flask, render_template, request, redirect, url_for
from Caller import get_aud_data
from textToAudio import getAudio
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index3.html', submitted_phrase=None, audio_url=None)


@app.route('/submit', methods=['POST'])
def submit():
    input_string = request.form['phrase']
    sampling_rate = 32000
    aud_data = get_aud_data(input_string)
    file_name = getAudio(aud_data, sampling_rate, input_string)

    # You can use a fixed audio file path or generate it dynamically.
    # Here, we use a fixed audio file.
    audio_filename = "audioFiles/" + file_name
    audio_url = url_for('static', filename=audio_filename)

    return render_template('index3.html', submitted_phrase=input_string, audio_url=audio_url)


if __name__ == '__main__':
    app.run(debug=True)
