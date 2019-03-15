from flask import Flask
from flask import request

myapp = Flask(__name__)

@myapp.route('/booksearch', methods=['GET'])
def booksearch():
    title = request.args.get('title')
    author = request.args.get('author')
    return '{1}さんの本「{0}」ですね。お探しします'.format(title,author)