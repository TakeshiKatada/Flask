from flask import Flask

myapp = Flask(__name__)

@myapp.route('/')
def index():
    return '''
    <h2>Flaskの練習サイトです</h2>
    <p><a  href="/hello">Helloページへ</a></p>
    '''

@myapp.route('/hello')
def hello():
    return 'こんにちは'