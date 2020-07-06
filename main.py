from flask import Flask,render_template
from os import listdir
app = Flask(__name__)

@app.route('/')
def index():
    returning_file_list = listdir("static/Downloads/")
    return render_template("index.html",list_of_files=returning_file_list)

@app.route('/upload-data')
def upload_data():
    pass

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    pass
# app.run(debug=True,host='192.168.225.174',port=5000) Production mode
app.run(debug=True)