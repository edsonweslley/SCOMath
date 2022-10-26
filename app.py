from fileinput import filename
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime
import constants as cte
import os

def allowed_file(filename):
    return '.' in filename and \
            filename.split('.', 1)[1].lower() in cte.ALLOWED_EXTENSIONS


def create_app():
    app = Flask(__name__)

    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        if request.method == 'POST':
            file = request.files['POST']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                new_filename = f'{filename.split(".")[0]}_ \
                                        {str(datetime.now())}.csv'
                file.save(os.path.join('input', new_filename))

            return 'aiaiai'

        return render_template('upload.html')
    return app
