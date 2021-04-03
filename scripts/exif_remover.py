import os
import PIL.Image
from scripts.ed.exif_delete import run_exif_delete

filetypes = [".jpg", ".png", ".jpeg", ".gif", ".tiff"]

def exif_cleanse(dir):
    exif_files = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if any([file.endswith(ft) for ft in filetypes]):
                 path = os.path.join(root, file)
                 if get_exif_data(path) != None:
                     exif_files.append(path)

    if len(exif_files)<1: return

    out = '\n'.join(exif_files)
    print("\nWARNING: Found EXIF tags in following files: \n" + out)

    print("\nRemove EXIF data now?")
    choice = input().lower()
    if choice in ['yes', 'y', 'ye', '']:
        for file in exif_files:
            run_exif_delete(['', '--replace', file])

def get_exif_data(path):
    img = PIL.Image.open(path)
    return img._getexif()
