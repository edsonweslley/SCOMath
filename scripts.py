import zipfile
import constants as cte
import pathlib


def extract_zip(path, filename):
    with zipfile.ZipFile(path + filename, 'r') as zip_ref:
        zip_ref.extractall(path + filename.split(".")[0])
    return (str(path + filename))


def zip_folder(path, foldername):
    foldername = pathlib.Path(path + foldername)
    with zipfile.ZipFile(str(foldername) + ".zip", mode="w") as archive:
        for file_path in foldername.rglob("*"):
            archive.write(
                file_path,
                arcname=file_path.relative_to(foldername)
                )
    return (str(foldername))


# def create_question(id, text, type, answers, correctAnswer, objectiveId):
#     question = f"""
# test.AddQuestion(new Question ("{id}",\n
#                                 "{text}",\n
#                                 {type},\n
#                                 {answers},\n
#                                 {correctAnswer},\n
#                                 "{objectiveId}"\n)
#                 );
#     """
#     with open('teste.js', 'w') as file:
#         for line in question.split('\n'):
#             file.write(line + '\n')


def create_question(text, correctAnswer, step):
    question = f"""
test.AddQuestion(new Question ("com.scorm.golfsamples.interactions.playing_{step}",\n
                                "{text}",\n
                                QUESTION_TYPE_NUMERIC,\n
                                null,\n
                                "{correctAnswer}",\n
                                "obj_playing"\n)
                );
    """
    with open(cte.PATH_QUESTIONS, 'a') as file:
        for line in question.split('\n'):
            file.write(line + '\n')


def blank_question_file():
    with open(cte.PATH_QUESTIONS, 'w') as fout:
        fout.write('')


def create_name_question(text):
    html_base = open('htmlbase.html', 'r', encoding='utf-8')
    string_html_base = ""
    for e in html_base:
        string_html_base += e
    name_question = f"""
<h1>{text}</h1>
<script type="text/javascript">
RenderTest(test);
</script>
</body>
</html>
    """
    final_html = string_html_base + name_question
    with open(cte.PATH_ASSESSMENT, 'w', encoding='utf-8') as file:
        file.write(final_html)




path = cte.PATH_INPUT
filename = 'SequencingSimpleRemediation_SCORM20043rdEdition.zip'
foldername = filename.split(".")[0]

# zip_folder(path, foldername)

# extract_zip(path, filename)

# create_question("com.scorm.golfsamples.interactions.fun_3",
#                 "You should take your score very seriously if you
# want to have a lot of fun on the course.",
#                 "QUESTION_TYPE_TF",
#                 "null",
#                 "false",
#                 "obj_havingfun")

# blank_question_file()
# x = 

# y = ""
# for e in x:
#     # print(str(e))
#     y += e

# # with open('htmlbase.html', 'a') as file:
# #     file.write('teste')

# y = y[:len(y)-105:]

# z = open('novohtml.html', 'w', encoding='utf-8')
# z.write(y)