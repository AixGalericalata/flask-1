from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/list_prof/<list>')
def training(list):
    param = {}
    param['list'] = list
    return render_template('nigger.html', **param)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
