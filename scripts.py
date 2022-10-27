import zipfile
import shutil
import constants as cte


def extract_zipfile(path, filename):
    with zipfile.ZipFile(path + filename, 'r') as zip_ref:
        zip_ref.extractall(path + filename.split(".")[0])


def zip_folder(path, foldername):
    shutil.make_archive(foldername, 'zip', path)


path = 'C:/Users/edson/Documents/TCC/TCC/input/'
filename = 'SequencingSimpleRemediation_SCORM20043rdEdition.zip'
foldername = path + filename.split(".")[0]

extract_zipfile(path, filename)
zip_folder(path, foldername)
