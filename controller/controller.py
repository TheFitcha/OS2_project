from tkinter import filedialog as fd
import model.data_models as models
from helper_methods import AES_functions as aes_f
from helper_methods import RSA_functions as rsa_f
from helper_methods import hash_functions as hash_f
from helper_methods import signature_functions as sign_f

FILETYPES = (('text files', '*.txt'), ('All files', '*.*'))

class Controller:
    def __init__(self, view) -> None:
        self.view = view

    # method key: AES, RSA_public, RSA_private
    # method data: AES, RSA, HASH, SIGNATURE
    def load_file(self, type, method):
        file = fd.askopenfile(filetypes=FILETYPES)
        filename = ''
        which_to_show = ''
        value = ''
        if file:
            if type == 'key':
                models.loaded_keys[method] = {'filename': file.name, 'key': ''.join(file.readlines())}
                value = models.loaded_keys[method]['key']
            elif type == 'data':
                models.loaded_data[method] = {'filename': file.name, 'value': ''.join(file.readlines())}
                value = models.loaded_data[method]['value']
            else:
                raise Exception(f'Wrong type received ({type}), expected key or data!')
        else:
            raise FileNotFoundError('File not selected!')

        filename = file.name.split('/')[-1]
        if method == 'AES' and type == 'key':
            which_to_show = 'key'
        elif method == 'RSA_public' and type == 'key':
            which_to_show = 'key_public'
        elif method == 'RSA_private' and type == 'key':
            which_to_show = 'key_private'
        elif method == 'AES' and type == 'data':
            which_to_show = 'data'
        elif method == 'RSA' and type == 'data':
            which_to_show = 'data'
        elif method == 'HASH' and type == 'data':
            which_to_show = 'data'
        elif method == 'SIGNATURE_public' and type == 'key':
            which_to_show = 'key_public'
        elif method == 'SIGNATURE_private' and type == 'key':
            which_to_show = 'key_private'
        elif method == 'SIGNATURE' and type == 'data':
            which_to_show = 'data'
        elif method == 'SIGNATURE_sign' and type == 'key':
            which_to_show = 'sign'

        self.view.show_data(which_to_show, filename, value)

    #region AES
    def generate_AES_key(self):
        key = aes_f.aes_derive_key()
        fileKey = fd.asksaveasfile(mode='w', defaultextension='.txt', initialfile="AES_key.txt")

        if fileKey is None:
            return

        fileKey.write(key.decode('latin-1'))
        fileKey.close()

        
    def AES_encrypt(self, mode="CTR"):
        if models.loaded_keys['AES']['key'] == '':
            raise ValueError("Key for AES not loaded!")
            
        if models.loaded_data['AES']['value'] == '':
            raise ValueError("Data for encryption not loaded!")
        
        encrypted_data = aes_f.aes_encrypt(models.loaded_data['AES']['value'], models.loaded_keys['AES']['key'], mode)
        self.view.show_aes_result(encrypted_data)

    def AES_decrypt(self):
        if models.loaded_keys['AES']['key'] == '':
            raise ValueError("Key for AES not loaded!")
            
        if models.loaded_data['AES']['value'] == '':
            raise ValueError("Data for decryption not loaded!")

        decrypted_data = aes_f.aes_decrypt(models.loaded_data['AES']['value'], models.loaded_keys['AES']['key'])
        self.view.show_aes_result(decrypted_data)

    #endregion

    #region RSA
    def generate_RSA_key(self):
        private_key, public_key = rsa_f.generate_rsa_keys()
        fileKey = fd.asksaveasfile(mode='w+', defaultextension='.txt', initialfile="RSA_private_key.txt")

        if fileKey is None:
            return

        fileKey.write(private_key.decode('utf-8'))
        fileKey.close()

        fileKey = fd.asksaveasfile(mode='w+', defaultextension='.txt', initialfile="RSA_public_key.txt")

        if fileKey is None:
            return

        fileKey.write(public_key.decode('utf-8'))
        fileKey.close()


    def RSA_encrypt(self):
        if models.loaded_keys['RSA_public']['filename'] == '':
            raise ValueError("Public key for RSA not loaded!")

        # if models.loaded_keys['RSA_private']['key'] == '':
        #     raise ValueError("Private key for RSA not loaded!")
            
        if models.loaded_data['RSA']['filename'] == '':
            raise ValueError("Data for decryption not loaded!")

        encrypted = rsa_f.encrypt_data(models.loaded_data['RSA']['value'], models.loaded_keys['RSA_public']['key'])
        self.view.show_rsa_result(encrypted)

    def RSA_decrypt(self):
        # if models.loaded_keys['RSA_public']['key'] == '':
        #     raise ValueError("Public key for RSA not loaded!")

        if models.loaded_keys['RSA_private']['filename'] == '':
            raise ValueError("Private key for RSA not loaded!")
            
        if models.loaded_data['RSA']['filename'] == '':
            raise ValueError("Data for decryption not loaded!")

        decrypted = rsa_f.decrypt_data(models.loaded_data['RSA']['value'], models.loaded_keys['RSA_private']['key'])
        self.view.show_rsa_result(decrypted)

    #endregion

    #region HASH
    def generate_hash(self, type="sha256"):
        if models.loaded_data['HASH']['filename'] == '':
            raise ValueError("Hash data not loaded!")

        hashed = hash_f.generate_hash_sha256(models.loaded_data['HASH']['value'])
        self.view.show_hash_result(hashed)
        
    #endregion

    #region SIGNATURE
    def generate_sign_keys(self):
        private_key, public_key = sign_f.create_key()
        fileKey = fd.asksaveasfile(mode='w+', defaultextension='.txt', initialfile="signature_private_key.txt")

        if fileKey is None:
            return

        fileKey.write(private_key.decode('latin-1'))
        fileKey.close()

        fileKey = fd.asksaveasfile(mode='w+', defaultextension='.txt', initialfile="signature_public_key")

        if fileKey is None:
            return

        fileKey.write(public_key.decode('latin-1'))
        fileKey.close()

    def sign_file(self) -> str:
        if models.loaded_data['SIGNATURE']['filename'] == '':
            raise ValueError("Signature data not loaded!")

        signed = sign_f.sign(models.loaded_data['SIGNATURE']['value'], models.loaded_keys['SIGNATURE_private']['key'])
        self.view.show_signature_result('sign', signed)

    def check_file(self):
        if models.loaded_data['SIGNATURE']['filename'] == '':
            raise ValueError("Signature data not loaded!")
        if models.loaded_keys['SIGNATURE_public']['filename'] == '':
            raise ValueError("Public signature key not loaded!")
        if models.loaded_keys['SIGNATURE_sign']['filename'] == '':
            raise ValueError("Sign for digital signature not loaded!")

        check = sign_f.check(models.loaded_data['SIGNATURE']['value'], models.loaded_keys['SIGNATURE_public']['key'], models.loaded_keys['SIGNATURE_sign']['key'])  
        result = "Ispravno" if check else "Neispravno"
        self.view.show_signature_result('check', result)
    #endregion



        
        
        
    