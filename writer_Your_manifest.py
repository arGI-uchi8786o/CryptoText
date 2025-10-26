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
along with this program.If not, see <https://www.gnu.org/licenses/>.
"""
# version: 1.2: binary support
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
import random
import hashlib
import datetime

now = datetime.datetime.now()
ULTRA_RARE_PREMIUM_PASCHALE = False

pashcal = False
if '--secret-key=WINDOWSDRIVERCAT' in sys.argv:
    pashcal = True
if now.month == 12 and now.day == 31:
    print("HAPPY NEW YEAR!")
    ULTRA_RARE_PREMIUM_PASCHALE = True

    print(input("Hhahahah!").encode('cp1251'))
pashcal = False
if random.random() < 0.1:
    pashcal = True
if now.month == 2 and now.day == 21:
    pashcal = True
    
if random.random() < 0.001:
    ULTRA_RARE_PREMIUM_PASCHALE = True
    print("LEGENDARY PASCHALE ACTIVATED!💎🏆")
if ULTRA_RARE_PREMIUM_PASCHALE:
    print("ACTIVATED: GOLD UI-MODE!🎨")
def rainbow_print(text, duration=3, end='\n'):
        import time
        import math
       
    
        rainbow_colors = [
            "\033[38;2;255;0;0m",      # Красный
            "\033[38;2;255;127;0m",    # Оранжевый 
            "\033[38;2;255;255;0m",    # Ярко-желтый (золотой)
            "\033[38;2;0;255;0m",      # Зеленый
            "\033[38;2;0;0;255m",      # Синий
            "\033[38;2;75;0;130m",     # Индиго
            "\033[38;2;148;0;211m",    # Фиолетовый
            "\033[38;2;255;215;0m",    # Золотой
            "\033[38;2;255;255;100m",  # Неоново-золотой
        ]
       
        
        border_length = len(str(text)) + 4
        top_border = "✨" + "⭐" * (border_length - 2) + "✨"
        bottom_border = "✨" + "⭐" * (border_length - 2) + "✨"
       
        start_time = time.time()
        frame_count = 0
       
        while time.time() - start_time < duration:
            frame_count += 1
           
        
            if frame_count % 15 == 0:
                top_border = "🌟" + "💎" * (border_length - 2) + "🌟"
                bottom_border = "🌟" + "💎" * (border_length - 2) + "🌟"
            else:
                top_border = "✨" + "⭐" * (border_length - 2) + "✨"
                bottom_border = "✨" + "⭐" * (border_length - 2) + "✨"
           
        
            print('\033[2K\r', end='')  
           
            
            color_idx = int((time.time() * 40) % len(rainbow_colors))
            print(f"{rainbow_colors[color_idx]}{top_border}")
           
            
            rainbow_text = ""
            text_str = str(text)
            for i, char in enumerate(text_str):
                color_idx = int((time.time() * 50 + i * 2) % len(rainbow_colors))
                rainbow_text += f"{rainbow_colors[color_idx]}{char}"
           
            print(f"{rainbow_colors[color_idx]}✨ {rainbow_text} ✨")
           
        
            color_idx = int((time.time() * 30 + 2) % len(rainbow_colors))
            print(f"{rainbow_colors[color_idx]}{bottom_border}")
           
        
            print('\033[3A', end='')
           
            time.sleep(0.1)  
       
        
        print('\033[2K\r', end='')  
        GOLD = "\033[38;2;255;215;0m"
        final_border = "🏆" + "⭐" * (border_length - 2) + "🏆"
        print(f"{GOLD}{final_border}")
        print(f"{GOLD}✨ {text} ✨") 
        print(f"{GOLD}{final_border}{end}", end='')
 


if len(argv) > 1 and argv[1] in ['help', '--help', '-h', '/help', 'h']:
    print("usage: [gen/ungen/pack/] [NAME MANIFEST] [TEXT MANIFEST] [--debug-mode-on], [--metadata-remove]")
    print(f"example: {__file__} gen mymanifest 'manifest text test'")
    print("gen - generate manifest 🧾 -> 📦 -> 🔐 ->  🛡 ")
    print("ungen - decode manifest and write to console text🔓")
    print("pack - pack manifest to 1 file '(manifest name)'.zip🛠")
    print('AAAAAAAAAAAAA')
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
        if ULTRA_RARE_PREMIUM_PASCHALE:
            rainbow_print("[INFO] DONE!🎁")
        exit(0)



    except FileNotFoundError:
        print(colors.RED + "[ERROR] Manifest not found.")
    except FileExistsError:
        print(colors.RED + "[INFO] {name}_packed.zip already exists!")
        exit(1)
    
    
#self.AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA_BLYAAAT(PONOS(((((((((((((((((((((99))))))))))))))))))))))
if len(argv) > 2 and argv[1] == 'ungen':
    name = argv[2]
    manifest_dir = f'MANIFEST_{name}'
    try:
        with open(f'{manifest_dir}/Dec_info.txt', 'r') as f:
            key, nonce, tag = [b64decode(line.split(': ')[1].strip()) for line in f.readlines()[:3]]
            is_binary = (True if 'is_binary: True' in f.read() else False)
        with open(f'{manifest_dir}/main_manifest.bin', 'rb') as f:
            encrypted = f.read()

            
    except FileNotFoundError:
        print(colors.BLUE + "[ERROR] Manifest not found.")
        
        exit(1)
    
    except PermissionError:
        print(colors.RED + '[ERROR] PERMISSION DENIED!')
        exit(1)
    except RuntimeError as e:
        print(colors.RED + f'[ERROR] Runtime Error: {e}')
        exit()
    if ULTRA_RARE_PREMIUM_PASCHALE:
        print("")


    cipher = Cipher(algorithms.AES256(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted) + decryptor.finalize()

    if is_binary:
        with open(f'{manifest_dir}_decrypted', 'wb') as f:
            f.write(decrypted)
    else:
        with open(f'{manifest_dir}_decrypted', 'w') as f:
            try:
                f.write(decrypted.decode('utf-32-be'))
                print(colors.GREEN + '[INFO] SUCCESS.')
    
            except Exception as e:
                print(colors.RED + f'[ERROR]: {e}')

    
    exit(0)
debug_mode = False

if len(argv) > 4:
    if  '--debug-mode-on' in sys.argv:
        print(colors.CYAN + "DEBUGGING MODE ACTIVATED.")
        debug_mode = True
if ULTRA_RARE_PREMIUM_PASCHALE:
    rainbow_print("[⚠WARNING⚠] ⚒Supported⚒ Only NON-BINARY🗄 Files.")
    rainbow_print("[IN❗FO] For binary, Use: zip📦, rar📦, 7zip📦 with passwords🔑")
else:
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
                print(colors.RED + "[ERROR] File not found.")
                
                exit(0)
        if '--this-is-file' in sys.argv or '--this-file' in sys.argv or ['--', '--is-file', '--file'] in sys.argv:
            print("[WARNING] flag not 'file' not found.Did you mean '--this-is-a-file'?")
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
                    
                    if isinstance(datass, bytes):
                        plaintext = datass
                    else:
                        plaintext = datass.encode('utf-32-be')
                sys.argv = [arg for arg in sys.argv if arg != "--this-is-a-file"]
            except FileNotFoundError:
                print(colors.RED + "[ERROR] File not found.exiting.")
                exit(0)

        
      

    


else:
    name = input("ENTER NAME OF YOUR MANIFEST: ")
    import getpass
    plaintext = getpass.getpass("ENTER YOUR MANIFEST: ").encode('utf-32-be')
    

if debug_mode:
    print(colors.GREEN + "[DEBUG] generating path to manifest")
manifest_path_project = f'MANIFEST_{name}'
if plaintext == 'HAHAHAHAHAHAHA'.encode('utf-32-be'):
    print(colors.GREEN + "AHA!")

if debug_mode:
    print(colors.GREEN + "[DEBUG] makind directory for manifest")
try:
    mkdir(manifest_path_project)
except FileExistsError:
    print(colors.RED + "[ERROR] Manifest ALREADY exists.")
    exit(1)
if ULTRA_RARE_PREMIUM_PASCHALE:
    rainbow_print("[INFO] building🛡🔐🔨 Main📦 Manifest📃...")
    print(f"{os.getlogin()}, Вы везунчик!")

print(colors.BLUE + "[INFO] making main manifest...")

with open(f'{manifest_path_project}/main_manifest.bin', 'wb') as f:
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
if ULTRA_RARE_PREMIUM_PASCHALE:
    manifest_id = 7777

hash = hashlib.sha256(plaintext_encrypted, usedforsecurity=True).hexdigest()
print(colors.BLUE +  "[INFO] making Dec_info.txt...")
with open(f"{manifest_path_project}/Dec_info.txt", 'w')as f:
    f.write(f"KEY: {b64(key).decode('ascii')}\n")
    f.write(f"NONCE: {b64(nonce).decode('ascii')}\n")
    f.write(f"TAG: {b64(tag).decode('ascii')}\n")
    f.write(f"MANIFEST_ID: {manifest_id}")
print(colors.BLUE + "[INFO] making metadata for manifest...")
if '--metadata-remove' in sys.argv or '--remove-metadata' in sys.argv:
    print(colors.RED + "[INFO] Metadata removed by user.So, skip this step...")
else:
    with open(f"{manifest_path_project}/metadata.txt", 'w') as f:
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
        f.write(f"CHECK_HASH_SUM: {hash}\n")
        if pashcal:
            f.write("SECRET_PASCHAL_EAG_ACTIVATED!!!\n")
        if ULTRA_RARE_PREMIUM_PASCHALE:
            f.write("USER_IS_PREMIUM_VIP: TRUE\n")
        
  
if debug_mode:
    with open(f"{manifest_path_project}/Debug_decrypted_manifest(DeleteMe).txt", 'wb') as f:
        f.write(plaintext)
    print("delete file 'Debug_Decrypted_manifest(DeleteMe).txt' later, please. ")
if pashcal or ULTRA_RARE_PREMIUM_PASCHALE:
    print('\n\n\n\n')
    print("HHEHEHEHEHEH:)")
    print(colors.MAGENTA + "PASCHAL EGG ACTIVATED!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(f"Your login: {os.getlogin()}")
    print(f"Your OS: {platform()}")
    import platform
    print(f"Your Machine Status: {platform.machine()}")
    print(f"Your Architecture: {platform.architecture()}")
    print(f"Your processor: {platform.processor()}")
    print(f"Your System Release: {platform.release()}")
    print(f"Your python build: {platform.python_build()}")
    print(f"Your python compiler:{platform.python_compiler()}")
    print(f"Your python version: {platform.python_version()}")
    print(f"Your android(If you on phone,not for desktop computer/laptop): {platform.android_ver()}")
    print(f"Current time: {get_time()}")
    print(f"OS: {platform.system()}")
if ULTRA_RARE_PREMIUM_PASCHALE:
    print('\n\n\n\n\n\n\n')
    rainbow_print("You are VIP.Done!")
    rainbow_print(f"Вам Подарок:{os.getlogin()}...")
    rainbow_print("🎁🎁🎁")

