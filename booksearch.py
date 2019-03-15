from flask import Flask
from flask import request
from flask import render_template

myapp = Flask(__name__)

@myapp.route('/searchform', methods=['GET'])
def searchform():
    renderpage = render_template("searchform.html")
    return renderpage

@myapp.route('/result', methods=['POST'])
def show_result():
    title = request.form['title']
    author = request.form['author']
    the_result = '<p>{1}さんの本[{0}]ですね。お探しします</p>'.format(title,author)
    link_back = '<p><a href="/searchform">検索フォームへ</a>'
    return the_result + link_back