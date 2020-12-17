from flask import Flask, render_template, jsonify
from random import *

DEBUG = True

app = Flask(__name__,
            static_folder='../dist/static',
            template_folder='../dist'
           )
app.config.from_object(__name__)

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()