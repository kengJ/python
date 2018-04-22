from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import make_response


app = Flask(__name__)
@app.route("/")
def helloword():
    return render_template('index/index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=80,debug=True)
