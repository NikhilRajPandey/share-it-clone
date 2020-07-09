from flask import Flask,render_template,request,redirect,url_for,abort,send_from_directory
from werkzeug.utils import secure_filename
from os import listdir,getcwd,path
import json
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/VerySecret'
app.config['UPLOAD_FOLDER'] = getcwd() + '/downloads'

# Opening the config file
def open_config():
    config_file = open('param.json','r')
    param = json.load(config_file)
    config_file.close()
    return param
    
params = open_config()

def increment_uploads():
    global params
    params['uploads'] = params['uploads'] + 1 # This is for local variable
    with open('param.json','w') as param_in_written:
        param_in_written.write(json.dumps(params,indent=4))
# I have open this file in write mode to update upload values and then i write pass because i want that this file should close automaticaly as the program exit

def isinAllowedExtensions(filename):
    # I have selected here the last splited because sometimes filename can also be like xyz.ex.ex2
    if filename.split('.')[-1] in params['NonAllowedExtensions']:
        return False
    return True

def get_index(item,array):
    try:
        return array.index(item)
    except:
        return -1
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload-data',methods=['GET','POST'])
def upload_data():
    if request.method == 'POST':
        files_ = request.files.getlist('your_file')
        unique_code = request.form['unique_code']
        if files_ and unique_code:
            if not params['uploads_files'].get(unique_code):
                # Means It is first file that is going to upload in this unique_code
                params['uploads_files'][unique_code] = []
            for file in files_:
                file_name = secure_filename(file.filename)
                if isinAllowedExtensions(file_name):
                    params['uploads_files'][unique_code].append(file_name)
                    file.save(path.join(app.config['UPLOAD_FOLDER'], file_name))
                    # Uploading Data ^^^
                else:
                    return "Wrong Extensions"
            # Syntax copied from https://www.roytuts.com/python-flask-multiple-files-upload-example/ but i have just make it as one liner
            increment_uploads() # And this is for file
            return redirect(f'/download-data?unique_code={unique_code}')
        return "No File Selected"
    abort(404)

@app.route('/download-file')
def download_file():
    unique_code = request.args.get('unique_code','')
    file_name = request.args.get('file','')
    if unique_code and file_name:
        is_correct_uniqcode = params['uploads_files'].get(unique_code)
        is_correct_filename = get_index(file_name,is_correct_uniqcode)
        if is_correct_uniqcode and is_correct_filename != -1:
            return send_from_directory(app.config['UPLOAD_FOLDER'],
                                    file_name, as_attachment=True)
    abort(404)

@app.route('/download-data')
# In this url all the data will be displayed and option to download them
def download_data():
    unique_code = request.args.get('unique_code','')
    if unique_code:
        files_at_this_unique_code = params['uploads_files'].get(unique_code)
        if files_at_this_unique_code:
            return render_template('download.html',list_of_files=files_at_this_unique_code)
    abort(404)
    

@app.route('/delete')
def logout():
    pass
# app.run(debug=True,host='192.168.225.174',port=5000)
app.run(debug=True)