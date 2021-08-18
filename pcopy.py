#!/usr/bin/env python3 

import argparse
from utils import utils as u

ap = argparse.ArgumentParser(description="Copy pre defined list of camera RAW files to a new folder. See more at <https://github.com/madhurangar/photo-copier>")
ap.add_argument('input', type=str, help='Text file containing the selected files list to be coppied over')
ap.add_argument('-n', '--folder-name', type=str, help='Folder (name) to copy files over', default="selected_photos")
# ap.add_argument('-f', '--force-copy', type=bool, help='Overwrite files already in the selected-photos folder', default=False)
ap.add_argument('-f', '--force-copy', help='Overwrite files already in the selected-photos folder', action='store_true')
ap.add_argument('-t', '--filetypes', nargs='+', type=str, help='File extensions (defaults: NEF ARW CR2 CR3 DNG and CRW)', default=['.NEF', '.ARW', '.CR2', '.CR3', '.DNG', '.CRW'])
args = ap.parse_args()

cwd = u.get_cwd()
filenames = u.read_file(args.input)

extensions = u.create_extensions_list(args.filetypes)
force_copy = args.force_copy
photos_folder = args.folder_name


filepaths = u.create_files_list(filenames, extensions, cwd, photos_folder )
u.copy_files(filepaths,cwd, photos_folder, force_copy)

