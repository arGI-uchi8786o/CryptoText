""""
This is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

this program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
GNU General Public License for more details.

You should have a received a copy of GNU General Public License
along with this progrsm.If not, see <https://www.gnu.org/licenses/>.
"""
from random import randint
from secrets import token_bytes
from cryptography.hazmat.primitives.ciphers import algorithms, modes, Cipher
from cryptography.hazmat.backends import default_backend
from os import mkdir
from sys import argv
from base64 import b64encode as b64
from colorama import init as colorama_init
colorama_init()
from colorama import Fore as colors
from time import ctime as get_time
from os import getlogin
from platform import platform
import os
import sys 
from base64 import b64decode
import zipfile
global IS_FILE
IS_FILE = False
import hashlib
if len(argv) > 1 and argv[1] in ['help', '--help', '-h', '/help', 'h']:
    print("usage: [gen/ungen/pack/] [NAME MANIFEST] [TEXT MANIFEST] [--debug-mode-on], [--metadata-remove]")
    print(f"example: {__file__} gen mymanifest 'manifest text test'")
    print("gen - generate manifest 🧾 -> 📦 -> 🔐 ->  🛡 ")
    print("ungen - decode manifest and write to console text🔓")
    print("pack - pack manifest to 1 file '(manifest name)'.zip🛠")
    exit(0)
if len(argv) > 2 and argv[1] == 'pack':
    print(colors.YELLOW + 'Packing your manifest...')
    name = argv[2]
    manifest_dir = f'MANIFEST_{name}'
    
    try:
        with zipfile.ZipFile(f'{name}_packed.zip', 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
            for root, dirs, files in os.walk(manifest_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    archname = os.path.relpath(file_path, manifest_dir)
                    zipf.write(file_path, archname)
                    print(colors.BLUE + f'[INFO] Added to archive: {archname}')
        print(colors.BLUE + "[INFO] Done!")
        exit(0)



    except FileNotFoundError:
        print(colors.RED + "[ERROR] Manifest not found.")
    except FileExistsError:
        print(colors.RED + "[INFO] {name}_packed.zip already exists!")
        exit(1)
    
    

if len(argv) > 2 and argv[1] == 'ungen':
    name = argv[2]
    manifest_dir = f'MANIFEST_{name}'
    try:
        with open(f'{manifest_dir}\\Dec_info.txt', 'r') as f:
            key, nonce, tag = [b64decode(line.split(': ')[1].strip()) for line in f.readlines()[:3]]
        with open(f'{manifest_dir}\\main_manifest.bin', 'rb') as f:
            encrypted = f.read()
    except FileNotFoundError:
        print(colors.BLUE + "[ERROR] Manifest not found.")
        exit(1)
    # НО НЕ НАДО ГЛОТАТЬ ИСКЛЮЧЕНИЯ КАК ХУИ!


    cipher = Cipher(algorithms.AES256(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted) + decryptor.finalize()

    print(decrypted.decode('utf-32-be'))
    exit(0)
debug_mode = False

if len(argv) > 4:
    if  '--debug-mode-on' in sys.argv:
        print(colors.CYAN + "DEBUGGING MODE ACTIVATED.")
        debug_mode = True
print("[WARNING] Supported only NON-BINARY Files.")
print('[INFO] For binary use: zip, rar, 7zip with passwords.')

manifest_id = randint(100000, 1000000)

if len(argv) > 3:
    if argv[1] == 'gen':

        name = argv[2]
        plaintext = argv[3].encode('utf-32-be')
        if '--this-is-a-file' in sys.argv:
            print(colors.BLUE + '[INFO] if you see this, flag --this-is-a-file enabled...')
            IS_FILE = True
            try:
                file_path = sys.argv[3]
                with open(file_path, 'rb') as f:
                    try:
                        datass = f.read().decode('utf-8')
                    except UnicodeDecodeError:
                        print(colors.RED + f"[ERROR] can't decode  {file_path} as utf-8.")
                        encoding = input(f"Please enter encoding of {file_path}: ")
                        datass = f.read().decode(encoding)
                    
                    plaintext = datass.encode('utf-32-be')
                sys.argv = [arg for arg in sys.argv if arg != "--this-is-a-file"]
            except FileNotFoundError:
                print(colors.RED + "[ERROR] File not found.exiting.")
                exit(0)
        if '--this-is-file' in sys.argv:
            print("[WARNING]--this-is-file flag not found.Did you mean '--this-is-a-file'?")
        
      

    


else:
    name = input("ENTER NAME OF YOUR MANIFEST: ")
    import getpass
    plaintext = getpass.getpass("ENTER YOUR MANIFEST: ").encode('utf-32-be')

if debug_mode:
    print(colors.GREEN + "[DEBUG] generating path to manifest")
manifest_path_project = f'MANIFEST_{name}'

if debug_mode:
    print(colors.GREEN + "[DEBUG] makind directory for manifest")
try:
    mkdir(manifest_path_project)
except FileExistsError:
    print(colors.RED + "[ERROR] Manifest ALREADY exists.")
    exit(1)
print(colors.BLUE + "[INFO] making main manifest...")

with open(f'{manifest_path_project}\\main_manifest.bin', 'wb') as f:
    if debug_mode:
        print(colors.GREEN + "[DEBUG] generating keys and nonce...")
    key = token_bytes(32)
    nonce = token_bytes(16)
    if debug_mode:
        print(colors.GREEN + "[DEBUG] encrypt data with AES...")
    cipher = Cipher(algorithms.AES256(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    plaintext_encrypted = encryptor.update(plaintext) + encryptor.finalize()
    tag = encryptor.tag

    if debug_mode:
        print(colors.GREEN + "[DEBUG] Writing generated text to file main_manifest.bin...")
    
    
    f.write(plaintext_encrypted)

def get_name():
    if len(argv) > 3 or len(argv) > 4:
        return argv[2]
    else:
        return name

hash = hashlib.sha256(plaintext_encrypted, usedforsecurity=True).hexdigest()
print(colors.BLUE + "[INFO] making Dec_info.txt...")
with open(f"{manifest_path_project}\\Dec_info.txt", 'w')as f:
    f.write(f"KEY: {b64(key).decode('ascii')}\n")
    f.write(f"NONCE: {b64(nonce).decode('ascii')}\n")
    f.write(f"TAG: {b64(tag).decode('ascii')}\n")
    f.write(f"MANIFEST_ID: {manifest_id}")
print(colors.BLUE + "[INFO] making metadata for manifest...")
if '--metadata-remove' in sys.argv or '--remove-metadata' in sys.argv:
    print(colors.RED + "[INFO] Metadata removed by user.So, skip this step...")
else:
    with open(f"{manifest_path_project}\\metadata.txt", 'w') as f:
        f.write(f"timestamp: {get_time()}\n")
        f.write(f"Name: {get_name()}\n")
        f.write(f"manifest_id: {manifest_id}\n")
        f.write(f"Author: {getlogin()}\n")
        f.write(f"System: {platform()}\n")
        f.write(f"Generated_By: {__file__}\n")
        f.write(f"Python_Version: {sys.version.split()}\n")
        f.write(f"Cryptography_backend: {default_backend().name}\n")
        f.write(f"process_id: {os.getpid()}\n")
        f.write(f"working_directory: {os.getcwd()}\n")
        f.write(f"Is_From_file: {IS_FILE}\n")
        f.write(f"BEING_DEBUGGING: {debug_mode}\n")
        f.write(f"CHECK_HASH_SUM: {hash}")
  
if debug_mode:
    with open(f"{manifest_path_project}\\Debug_decrypted_manifest(DeleteMe).txt", 'wb') as f:
        f.write(plaintext)
    print("delete file 'Debug_Decrypted_manifest(DeleteMe).txt' later, please. ")
