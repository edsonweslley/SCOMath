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


def create_question(id, text, type, answers, correctAnswer, objectiveId):
    question = f"""
test.AddQuestion(new Question ("{id}",\n
                                "{text}",\n
                                {type},\n
                                {answers},\n
                                {correctAnswer},\n
                                "{objectiveId}"\n)
                );
    """
    with open('teste.js', 'w') as file:
        for line in question.split('\n'):
            file.write(line + '\n')


def blank_question_file():
    with open('teste.js', 'w') as fout:
        fout.write('')


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
