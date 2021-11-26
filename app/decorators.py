import os
import shutil

from .exceptions import CreateFileError
from .exceptions import CreateFolderError


def raise_error(directory):
    if directory.is_file():
        raise CreateFileError(directory)
    
    elif directory.is_dir():
        raise CreateFolderError(directory)

    raise Exception('Was not possible to complete the task.')


def delete_dir(directory):
    if directory.is_file():
        os.remove(directory)
        
    elif directory.is_dir():
        shutil.rmtree(directory)


def check_if_dir_exists(function):
    
    def wrapper(dir, path, force=False, *args, **kwargs):
        directory = path / dir
        
        if directory.is_dir() or directory.is_file():
            
            print(dir)
            
            if directory.exists() and force:
                delete_dir(directory)

            response = function(dir, path, force)
            return response
        
        print(directory.is_dir())
        print(directory.is_file())
        print(directory.iterdir())
        print(directory)
        
        raise_error(directory)
    
    return wrapper
