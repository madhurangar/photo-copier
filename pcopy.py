#!/usr/bin/env python3 

import argparse
from utils import utils as u

PHOTOS_FOLDER = "selected_photos" # folder to copy new photos over 

ap = argparse.ArgumentParser(description="Copy pre defined list of camera RAW files to a new folder. See more at ")
ap.add_argument('input', type=str, help='Text file containing the selected files list to be coppied over')
ap.add_argument('-filetype', type=str, help='Raw photos file extension (default: crw)', default="CRW")
args = ap.parse_args()

cwd = u.get_cwd()
extension = args.filetype
filenames = u.read_file(args.input)

filepaths_list = u.create_files_list(filenames, extension, cwd, PHOTOS_FOLDER)
u.copy_files(filepaths_list,cwd, PHOTOS_FOLDER)
