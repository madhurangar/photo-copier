#!/usr/bin/env python3 

from sys import exit
import pathlib, shutil, tqdm

def abnormal_termination()->None:
    print(">Terminated with an error!")
    exit()


def read_file(file_name:str)->set:
    """read white-space separated text file and create a list

    Args:
        file_name (str): path to .txt file
    """
    try:
        with open(file_name, "r") as f:
            data = f.read().strip().split()
    except:
        print(f"ERROR: Can not open {file_name} file!")
        print("(file doesn't exist or may be in a different path)")
        abnormal_termination()
        
    # remove duplicates
    data_set = set(data)
    data_set.difference()

    return data_set


def clean_filename(filename:str)->str:
    """get file name with out the extension

    Args:
        filename (str): file name with or with out extension 
        or duplicate files (i.e. IMG1234 copy.jpg)

    Returns:
        str: cleaned filename
    """
    fname_split = filename.split()[0].split(".")[0].split("-")[0].split("_")[0]
    
    return fname_split
    

def create_extensions_list(extensions:list[str])->set:
    ext = set()
    for e in extensions:
        e = e.split(".")[-1]
        ext.add(f".{e.upper()}")
        
    return ext


def create_files_list(filenames:set, accepted_extensions:set, working_folder:pathlib.PosixPath, saving_folder:str) -> dict:
    """create a list of file paths to be copied

    Args:
        filenames (list): file names list from the text file
        accepted_extensions (set): raw file types
        working_folder (pathlib.PosixPath): path to working folder, where all the raw files are
        saving_folder (str, optional): path to the folder where photos gonna be coppied

    Returns:
        dict: list of full file paths {filename:filepath}
    """
    filepaths = dict()
    
    # current files in the saved files location if exists
    if pathlib.Path(working_folder/saving_folder).exists():
        current_saved_files = set(pathlib.Path(working_folder/saving_folder).glob('*.*'))
    else:
        current_saved_files = set()   
    
    # generate files list to copy
    for fname in filenames:
        cleaned_fname = clean_filename(fname)
        raw_files = set(working_folder.glob(f'**/{cleaned_fname}.*')) - current_saved_files
        files = [file for file in raw_files if file.suffix.upper() in accepted_extensions]
        if len(files) == 1:
            filepaths[files[0].name] = files[0]
        elif len(files) > 1:
            for fr in files:
                new_fname = f"{fr.stem} - {fr.parent.name}{fr.suffix}"
                filepaths[new_fname] = fr
    
    if not filepaths:
        print(">No files found!")
        abnormal_termination()
               
    return filepaths


def cp(src:pathlib.Path, dest:pathlib.Path)->None:
    """copy files from src (source) to dest (destination)

    Args:
        src (pathlib.Path): path of the source file
        dest (pathlib.Path): path of the destination
    """
    try:
        shutil.copy2(src, dest)
    except shutil.Error():
        print(f">ERROR: can't copy {src.name}")
        

def copy_files(filepaths:dict, working_folder:pathlib.Path, saving_folder:str, force_copy=False)->None:
    """copy RAW files to a new folder

    Args:
        filepaths_list (list): list of RAW files and their full path
        working_folder (pathlib.PosixPath): current working folder
    """ 
    # create folder to save new files if it doesn't exist
    pathlib.Path.mkdir(working_folder/saving_folder, exist_ok=True)
    save_path = working_folder/saving_folder
    
    if force_copy:
        print(">force-copy enabled: Overridding current files...")
    
    for fname, fpath in tqdm.tqdm(filepaths.items()):
        if not pathlib.Path(save_path/fname).exists():
            cp(fpath, save_path/fname)
        elif pathlib.Path(save_path/fname).exists() and force_copy:
            cp(fpath, save_path/fname)
        else:
            print(f">Skipping: {fname} already exists at destination")

def get_cwd():
    cwd = pathlib.Path.cwd()
    return cwd

