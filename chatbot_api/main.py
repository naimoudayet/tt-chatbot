from flask import Flask, request, jsonify

from controller import Controller
from bot.learn import webhook


app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def index():
    msg = request.json.get('msg')
    if msg:
        response = webhook(msg)

        return {
            'response': 'TEXT',
            'data': response,
        }

    return '200'


if __name__ == '__main__':
    app.run(port=5001)
