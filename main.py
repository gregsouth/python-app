from flask import Flask
import os
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/bye')
def byefornow():
    return 'Bye'


if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG') == 'True',
            host='0.0.0.0', port=os.environ.get('PORT'))
