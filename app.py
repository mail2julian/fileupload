from flask import *
import pandas as pd
import io
import csv
import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import pandas as pd
import pickle


UPLOAD_FOLDER = "E:/Prodevans/fileupload/upload/"
ALLOWED_EXTENSIONS = {'txt', 'csv','pkl','pdf', 'png', 'jpg', 'jpeg', 'gif'}
path='E:/Prodevans/fileupload/upload/model.pickle'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        try:
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                global name
                name=filename
                print("****************************",filename)
                              
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('uploaded_file', filename=filename)) 
        except:
            global df
            df=pd.read_csv(UPLOAD_FOLDER+name,error_bad_lines=False)
            dataa=df[0:5].to_html(classes='data')
            #print(dataa)
            return render_template('index1.html',tables=[dataa], titles='File Content')

    return render_template('index1.html')



 

#############################################################################3

'''@app.route('/')  
def upload():
    if request.method=='POST':
        if request.files:
            file=request.files["file"]
            file.save(os.path.join(app.config["IMAGE_UPLOADS"],
                                   file.filename))
            print("Successfully file saved")
    return redirect(request.url)  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        df=pd.read_csv(f)
        #print(df.head())
        f.save(f.filename)  
        return render_template("success.html", name = f.filename)  '''
  
if __name__ == '__main__':  
    app.run(debug = True) 
