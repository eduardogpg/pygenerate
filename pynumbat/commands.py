import os
import sys

import logging 

from .common import MAIN_CONTENT
from .common import README_CONTENT
from .common import GITIGNORE_CONTENT

from .common import SETUP_PY
from .common import SETUP_CFG
from .common import MIT_LICENSE

from .decorators import check_if_folder_exists


def create_file(path, content):
    with open(path, 'w') as file:
        file.write(content)

    return True


@check_if_folder_exists
def create_app_folder(folder, path='./', force=False):
    
    current_path = path / folder
    current_test_path = current_path / 'tests'
    
    os.makedirs(current_path)
    os.makedirs(current_test_path)

    create_file(current_path / '__init__.py', '')
    create_file(current_path / '__main__.py', MAIN_CONTENT)
    create_file(current_path / 'config.py', '')
    
    create_file(current_test_path / 'tests.py', '')


def create_basic_config(path, force=False, virtual_env=True, upload=False):
    try:
        create_app_folder('app', path, force)
        create_basic_files(path)
        
        if virtual_env:
            create_virtual_env(path)

        if upload:
            create_pypi_files(path)

    except Exception as err:
        logging.error(err)


def create_basic_files(path):
    create_file(path / 'main.py', MAIN_CONTENT)
    create_file(path / 'README.md', README_CONTENT)
    create_file(path / '.gitignore', GITIGNORE_CONTENT)


def create_pypi_files(path):
    create_file(path / 'setup.py', SETUP_PY)
    create_file(path / 'setup.cfg', SETUP_CFG)
    create_file(path / 'LICENSE.txt', MIT_LICENSE)


def create_virtual_env(path, environment='env'):
    try:
        if python_3_6_or_greater():
            os.system(f"cd {path} && python -m venv {environment}")
            create_requirementes_txt(path, environment)
        else:
            logging.warning('In order to create the virtual environment Python >3.6 its necessary.')
            
    except Exception as err:
        return False


def create_requirementes_txt(path, environment):
    try:
        if sys.platform.startswith('win'):
            os.system(f"cd {path} && . {environment}\Scripts\activate && pip freeze > requirements.txt")
        else:
            os.system(f"cd {path} && . {environment}/bin/activate && pip freeze > requirements.txt")
    except Exception as err:
        logging.error(err)
        

def python_3_6_or_greater():
    if sys.version_info[0] == 3 and sys.version_info[1] >= 3:
        return True