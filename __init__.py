from PIL import Image
from shutil import copyfile
import imagehash

import glob, os

IMG_DIR = 'img'
OUT_DIR = 'out'

os.chdir(IMG_DIR)
if not os.path.isdir(OUT_DIR):
    os.mkdir(OUT_DIR)
all_files_dict = {}

for file in glob.glob("*"):
    if not os.path.isfile(file):
        continue
    hash = imagehash.average_hash(Image.open(file))
    size = os.path.getsize(file)
    print(file, hash, size)
    if hash in all_files_dict:
        if all_files_dict[hash]['size'] > size:
            # We found a smaller file than before.
            continue

    # We found a new or bigger file. Update file infos.
    all_files_dict[hash] = {'size': size, 'file': file}

for hash in all_files_dict:
    file = all_files_dict[hash]['file']
    print('final file: ', file)
    copyfile(file, OUT_DIR + '/' + file)
