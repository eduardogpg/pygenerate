import os
from .decorators import check_if_dir_exists

from .common import MAIN_CONTENT
from .common import README_CONTENT
from .common import GITIGNORE_CONTENT


def create_file(path, content):
    with open(path, 'w') as file:
        file.write(content)
    
    return True


@check_if_dir_exists
def create_app_folder(folder, path='./', force=False):
    
    os.makedirs(folder)
    
    init_path = path / folder / '__init__.py'
    config_path =  path / folder / 'config.py'
    
    create_file(init_path, '')
    create_file(config_path, '')


def create_basic_config(current_location, force=False):
    try:
        create_app_folder('apps', current_location, force)
        # create_basic_files(current_location)
        
    except Exception as err:
        print(err)


def create_basic_files(current_location):
    create_file(current_location / 'mains.py', MAIN_CONTENT)
    create_file(current_location / 'READMEs.md', README_CONTENT)
    create_file(current_location / '.gitignores', GITIGNORE_CONTENT)