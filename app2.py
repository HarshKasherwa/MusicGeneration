import json

from flask import Flask, request, jsonify, render_template
from Caller import get_aud_data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index2.html')


@app.route('/api/echo', methods=['GET'])
def echo_string():
    input_string = request.args.get('input')
    print("input_string: ", input_string)
    aud_val = get_aud_data(input_string)
    lists = aud_val.tolist()
    json_str = json.dumps(lists)

    if input_string is not None:
        response_data = {
            'message': 'Received input:',
            'input': json_str
        }
        return jsonify(response_data)
    else:
        return jsonify({'error': 'Input parameter missing'})


if __name__ == '__main__':
    app.run(debug=True)
