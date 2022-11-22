from flask import Flask, request, render_template, redirect, \
    send_from_directory, url_for
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

    # list_questions = list()

    @app.route('/questions', methods=['GET', 'POST'])
    def questions():
        # print(request.form)
        # list_questions.append((
        #     request.form.get("id-question"),
        #     request.form.get("text-question"),
        #     request.form.get("type-question"),
        #     request.form.get("question-question"),
        #     request.form.get("answer-question"),
        #     request.form.get("objective-question")
        # ))
        # if len(list_questions) > 2:
        #     list_questions.clear()
        #       print(request.form)
        scripts.create_question(
            request.form.get("id-question"),
            request.form.get("text-question"),
            request.form.get("type-question"),
            request.form.get("question-question"),
            request.form.get("answer-question"),
            request.form.get("objective-question")
        )
        if request.method == "POST":
            return redirect(url_for('download'))
        return render_template('questions.html')

    @app.route('/download')
    def download():
        return render_template('download.html', files=os.listdir('input'))

    @app.route('/download/<filename>')
    def download_file(filename):
        return send_from_directory('input', filename)

    return app
