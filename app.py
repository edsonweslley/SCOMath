from flask import Flask, request, render_template, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
import constants as cte
import scripts
import os


def allowed_file(filename):
    return '.' in filename and \
            filename.split('.', 1)[1].lower() in cte.ALLOWED_EXTENSIONS


def create_app():
    app = Flask(__name__)

    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        if request.method == 'POST':
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                new_filename = filename
                save_location = os.path.join(cte.PATH_INPUT, new_filename)
                file.save(save_location)
                scripts.extract_zip(cte.PATH_INPUT, new_filename)
                return redirect(url_for('questions'))
        return render_template('upload.html')

    @app.route('/questions', methods=['GET', 'POST'])
    def questions():
        return render_template('questions.html')

    return app
