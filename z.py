from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/index/<text>')
def index(text):
    param = {}
    param['title'] = text
    return render_template('nigger.html', **param)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
