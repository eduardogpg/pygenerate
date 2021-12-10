import os
import shutil

from .exceptions import CreateFileError
from .exceptions import CreateFolderError


def raise_error(directory):
    if directory.is_file():
        raise CreateFileError(directory)
    
    elif directory.is_dir():
        raise CreateFolderError(directory)

    raise Exception('The task could not be completed.')


def delete_dir(directory):
    if directory.is_file():
        os.remove(directory)

    elif directory.is_dir():
        shutil.rmtree(directory)


def check_if_folder_exists(function):
    
    def wrapper(folder, path, force, *args, **kwargs):
        current_path = path / folder
            
        if current_path.exists() and force:
            delete_dir(current_path)

        response = function(folder, path, force, *args, **kwargs)
        return response
        
    return wrapper