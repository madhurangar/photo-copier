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
usage: pcopy.py [-h] [-filetype FILETYPE] input

Copy pre defined list of camera RAW files to a new folder. See more at <https://github.com/madhurangar/photo-copier>

positional arguments:
  input               Text file containing the selected files list to be
                      coppied over

optional arguments:
  -h, --help          show this help message and exit
  -filetype FILETYPE  Raw photos file extension (default: crw)
```

Looking for Windows installation instructions? see [here](installation-notes.md)