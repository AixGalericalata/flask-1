from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('nigger.html', **param)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
