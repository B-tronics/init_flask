import argparse
import os
import logging

# logging setup
logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

# get the project name, set default name to the current directory name
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", help="Projectname",
                default=os.getcwd().split('/')[-1])
project_name = vars(ap.parse_args())["name"]

folder_structure = [
    project_name,
    'tests',
    project_name+'/templates',
    project_name+'/templates/auth',
    project_name+'/templates/'+project_name,
    project_name+'/static',
]


def make_folders(project_name=project_name, folder_structure=folder_structure):
    for folder in folder_structure:
        try:
            os.makedirs(folder)
        except OSError as e:
            logger.error(e)
            exit()


files = [
    'setup.py',
    project_name+'/__init__.py',
    project_name+'/db.py',
    project_name+'/schema.sql',
    project_name+'/auth.py',
    project_name+'/templates/'+project_name+'/index.html',
    project_name+'/templates/base.html',
    project_name+'/static/style.css',
    project_name+'/templates/auth/register.html',
    project_name+'/templates/auth/login.html',
    'tests/conftest.py',
    'tests/db.sql',
    'MANIFEST.in',
]


def create_files(project_name=project_name, files=files):
    for file in files:
        try:
            f = open(file, "x")
            f.close()
        except FileNotFoundError as e:
            logger.error(e)
            exit()


if __name__ == '__main__':
    # create the folder structure
    make_folders()

    # create file structure
    create_files()

    logger.info("Project has been initialized.")
