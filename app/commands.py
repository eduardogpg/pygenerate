import os

from .common import MAIN_CONTENT
from .common import README_CONTENT
from .common import GITIGNORE_CONTENT

from .decorators import check_if_folder_exists

def create_file(path, content):
    with open(path, 'w') as file:
        file.write(content)
    
    return True


@check_if_folder_exists
def create_app_folder(folder, path='./', force=False):
    
    current_path = path / folder
    os.makedirs(current_path)

    create_file(current_path / '__init__.py', '')
    create_file(current_path / 'config.py', '')


def create_basic_config(path, force=False, virtual_env=True):
    try:
        create_app_folder('app', path, force)
        
        create_basic_files(path)
        
        if virtual_env:
            create_virtual_env(path)
        
    except Exception as err:
        print(">>>", err)


def create_basic_files(path):
    create_file(path / 'main.py', MAIN_CONTENT)
    create_file(path / 'README.md', README_CONTENT)
    create_file(path / '.gitignore', GITIGNORE_CONTENT)


def create_virtual_env(path, environment='env'):
    try:
        os.system(f"cd {path} && python3 -m venv {environment}")
        create_requirementes_txt(path, environment)
    except Exception as err:
        pass
    

def create_requirementes_txt(path, environment):
    try:
        os.system(f"cd {path} && . {environment}/bin/activate && pip freeze > requirements.txt ")
    except Exception as err:
        print(">>", err)