from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import make_response


app = Flask(__name__)
@app.route("/")
def helloword():
    return "helloword"

@app.route("/hello/<name>")
def hello1(name):
    return "name is %s" % name

@app.route("/hello/<int:number>")
def inputTest(number):
    return "number is %d" % number

@app.route("/hello/<float:number>")
def inputTest1(number):
    print(url_for("static",filename="test.css"))
    return "float is %f" % number

@app.route("/testGet",methods=['GET','POST'])
def getTest():
    if request.method == 'POST':
        return "post method"
    else:
        return "get method"

@app.route("/cookieT")
def cookieTest():
    if request.cookies.get('name')==None:
        resp = make_response(render_template("index.html"))
        repr.set_cookie('name','test')
    return resp

@app.route("/templ")
@app.route("/templ/<name>")
def templTest(name=None):
    return render_template("index.html",name=name,url="/cookieT")

@app.route("/testReq")
def testReq():
    error=None
    if request.method == 'GET':
        # print(request.form['username'])
        print(request.args.get('username',''))
    return "test"




if __name__ == '__main__':
    app.run(host='127.0.0.1',port=80,debug=True)
