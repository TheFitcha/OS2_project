from tkinter import filedialog as fd
import model.data_models as models

FILETYPES = (('text files', '*.txt'), ('All files', '*.*'))

def load_file(type, method):
    file = fd.askopenfile(filetypes=FILETYPES)
    if file:
        if type == 'key':
            models.loaded_keys[method] = {'filename': file.name, 'key': file.readlines()}
        elif type == 'data':
            models.loaded_data[method] = {'filename': file.name, 'value': file.readlines()}
        else:
            raise Exception(f'Wrong type received ({__name__})!')
    else:
        raise FileNotFoundError('File not selected!')
    