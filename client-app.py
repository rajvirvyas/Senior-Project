from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['UPLOAD_FOLDER'] = 'files'
class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired(), FileRequired(), FileAllowed(['png'], 'PNG Images Only!')])
    submit = SubmitField("Upload!")

@app.route('/', methods = ["GET", "POST"])
@app.route('/home', methods = ["GET", "POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file= form.file.data
        filename= secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        #file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return "Image Uploaded"
    # else:
    #     return "ONLY PNG FILES ALLOWED", 400

    return render_template('index.html', form=form)

if __name__ =="__main__":
    app.run(debug=True)
