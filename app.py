import json

from flask import Flask, request, jsonify, render_template
import pyttsx3
import tempfile
import os
from RW import read

from Caller import get_aud_data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/synthesize', methods=['POST'])
def synthesize_text():
    try:
        data = request.get_json()
        input_string = data['text']
        print("input_string: ", input_string)
        aud_val = read()
        sample_rate = 32000
        print("\naud_data: ", aud_val)
        lists = aud_val.tolist()
        json_str = json.dumps(lists)

        # Create a temporary WAV file for the synthesized speech
        # temp_wav_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
        #
        # # Synthesize the text to audio
        # engine = pyttsx3.init()
        # engine.save_to_file(text, temp_wav_file.name)
        # engine.runAndWait()

        # Prepare the response
        response_data = {
            'audioData': json_str,
            'sampleRate': sample_rate,
        }

        print("Data Sent")

        return jsonify(response_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
