pCopy
=====

This simple python script `pcopy` reads a list of file names and copies them to a separate folder. 

#### Pre-requisites 
 - Python 3 (ver. > 3.6)

#### How to use

Download / clone this repository to your computer (i.e `~/opt/photo-copier`). Then provide permission to execute script by it self. Finally, add it to `.zshrc` if you're using a Mac. 

```bash
cd ~/opt/photo-copier
chmod +x pcopy.py
echo 'alias pcopy="~/opt/photo-copier/pcopy.py"' >> ~/.zshrc
```

Now you should be able to use `pcopy` in the command line. 

#### Usage

```bash
pcopy -h                                           
usage: pcopy.py [-h] [-n FOLDER_NAME] [-f] [-t FILETYPES [FILETYPES ...]] [-s SEPARATE_CHARS [SEPARATE_CHARS ...]] input

Copy list of camera RAW files into a new folder. See more at <https://github.com/madhurangar/photo-copier>

positional arguments:
  input                 Text file containing the filenames (with or without file extensions)

optional arguments:
  -h, --help            show this help message and exit
  -n FOLDER_NAME, --folder-name FOLDER_NAME
                        Folder (name! not the path) to copy files over
  -f, --force-copy      Overwrite already coppied files
  -t FILETYPES [FILETYPES ...], --filetypes FILETYPES [FILETYPES ...]
                        Raw file extensions (defaults: NEF ARW CR2 CR3 DNG and CRW)
  -s SEPARATE_CHARS [SEPARATE_CHARS ...], --separate-chars SEPARATE_CHARS [SEPARATE_CHARS ...]
                        Split chars to construct the original RAW file name. e.g. extract "IMG12345" from "IMG12345-copy_new (1).ext" (defaults: . - and _ )
```

Looking for Windows installation instructions? see [here](installation-notes.md)