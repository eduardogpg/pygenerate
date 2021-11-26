class CreateFolderError(Exception):
    def __init__(self, folder):
        self.folder = folder
        self.message = f'Was not posible create "{folder}" folder.'
        
        super().__init__(self.message)


class CreateFileError(Exception):
    def __init__(self, file):
        self.file = file
        self.message = f'Was not posible create "{file}" file.'
        
        super().__init__(self.message)