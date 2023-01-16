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

    @app.route("/")
    def index():
        return redirect('/questions')

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

        text_question = request.form.getlist("text-question-field[]")
        answer_question = request.form.getlist("answer-question-field[]")
        statement_question = request.form.getlist("statement-question-field[]")

        if request.method == "POST":
            scripts.blank_question_file()
            for i in range(len(text_question)):
                scripts.create_question(text_question[i], answer_question[i], i + 1)
            scripts.create_name_question(statement_question[0])
            scripts.zip_folder(cte.PATH_PACOTE_BASE, cte.NAME_SCO)

            return send_from_directory(cte.PATH_PACOTE_BASE, cte.NAME_SCO + '.zip')
        return render_template('questions.html')

    @app.route('/download')
    def download():
        return render_template('download.html', files=os.listdir('pacote_base'))

    @app.route('/download/<filename>')
    def download_file(filename):
        return send_from_directory('pacote_base', filename)

    return app
