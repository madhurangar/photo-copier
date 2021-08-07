#!/usr/bin/env python3 

from sys import exit
import pathlib, shutil, tqdm


def abnormal_termination()->None:
    print(">Terminated with an error!")
    exit()


def read_file(file_name:str)->set:
    """
    Read white-space separated text file and create a list

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


def check_filename(filename:str, filetype:str) -> str:
    """check and correct file extensions.
    ie. IMG5678     -> IMG5678.CRW
        IMG5678.JPG -> IMG5678.CRW etc...
        
    * NOTE: Image file names "only" contain strings+integers 

    Args:
        filename (str): filename extracted from the text file
        filetype (str): raw file extension

    Returns:
        str: corrected filename
    """
    filename_split = filename.split(".")
    print(filename_split)
    if len(filename_split) == 1:
        new_filename = ".".join([filename, filetype])
    elif len(filename_split) == 2:
        new_filename = ".".join([filename_split[0], filetype])
    else:
        print(f"ERROR: Something's not right!. Please re-check the file list. (i.e. filename: {filename})")
        abnormal_termination()
           
    return new_filename


def create_files_list(filenames:set, filetype:str, working_folder:pathlib.PosixPath, saving_folder:str) -> list:
    """create a list of file paths to be copied

    Args:
        filenames (list): file names list from the text file
        filetype (str): raw file type
        working_folder (pathlib.PosixPath): path to working folder, where all the raw files are
        saving_folder (str, optional): path to the folder where photos gonna be coppied

    Returns:
        list: list of full file paths
    """
    filepaths_list = []
    print(working_folder/saving_folder)
    pathlib.Path.mkdir(working_folder/saving_folder, exist_ok=True)
    
    for file in filenames:
        # add/modify extension if not supplied in the text file
        corrected_filename = check_filename(file, filetype)
        try:
            # extract the full path to raw files. neglect PHOTOS_FOLDER
            # filepath = list(pathlib.Path(working_folder).rglob(corrected_filename))
            filepath = [path for path in pathlib.Path(working_folder).rglob(corrected_filename) if saving_folder not in path.parts[-2:]]
            if len(filepath) > 1:
                print(f"{corrected_filename}: multiple RAW files with same name!")
                # print(filepath)
            if filepath:
                filepaths_list.extend(filepath)
            else:
                print(f"{corrected_filename}: can not find RAW file")
        except:
            print(f"ERROR: something went wrong with {file}")
    
    return filepaths_list
        

def copy_files(filepaths_list:list, working_folder:pathlib.PosixPath, saving_folder:str)->None:
    """copy RAW files to a new folder

    Args:
        filepaths_list (list): list of RAW files and their full path
        working_folder (pathlib.PosixPath): current working folder
    """ 
    for file in tqdm.tqdm(filepaths_list):
        try:
            shutil.copy2(file, working_folder/saving_folder)
        except shutil.SameFileError:
            print(f"{file.name} already exists. skipping...")
        

def get_cwd():
    cwd = pathlib.Path.cwd()
    return cwd

