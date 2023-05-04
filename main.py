from flask import Flask, render_template, url_for, request
import database
import pandas as pd

app = Flask(__name__)

@app.route('/')
@app.route('/home',methods=['POST', 'GET'])
def home():
    return render_template("login.html")

@app.route('/profile',methods=['POST', 'GET'])
def login():
    output = request.form.to_dict()
    print(type(output['password']))
    # print(output)
    import database
    result = database.login(output['email'],output['password'])
    data = database.blog_data(result[1])
    import json
    final_data=json.loads(data)
    print(result)
    if result[0]== 'login':
        return render_template("profile.html",name=result[2],blogs=final_data)
    else:
        return render_template("login.html",result="Email or Password is wrong")

@app.route('/view',methods=['POST', 'GET'])
def view():
    return render_template("index.html")


@app.route('/view/<id>',methods=['POST', 'GET'])
def id_view(id):
    result=database.blog_data_id(id)
    if result[4]=='type1':
        print(result)
        return render_template("type1.html",title=result[1],body=result[2])
    else:
        return render_template("new_blog.html")


@app.route('/newblog',methods=['POST', 'GET'])
def newblog():
    return render_template("new_blog.html")

@app.route('/type1',methods=['POST', 'GET'])
def type1():
    import database
    result = database.type1()
    return render_template("type1.html",title=result[0],body=result[1])

@app.route('/register1/open',methods=['POST', 'GET'])
def register1open():
    return render_template("register1.html")

@app.route('/register1',methods=['POST', 'GET'])
def register1():
    output = request.form.to_dict()
    pic=request.files(output['image'])
    print(pic)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)