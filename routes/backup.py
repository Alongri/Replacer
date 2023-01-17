import os.path
import shutil
import sys
from pathlib import Path
from datetime import datetime

# Default values
import typer

CONST_BACKUP_DIR_NAME = "backups"
CONST_BACKUP_FILE_POSTFIX = "_rep"


# Removing extra copies of backups
def removing_extra_copies(backup_dir_path, file_name, backup_file_postfix, file_extension, how_many_copies):
    """
    Removing extra backup copies of a single file according to number of copies needed.

    Args:
        backup_dir_path (path): the path of the folder where the backup files are saved.
        file_name (str): name of the file.
        backup_file_postfix (str): backup postfix of the file name.
        file_extension (str):
        how_many_copies (int): how many backup files to keep back.

    Returns:
        void: none
    """
    allfiles = os.listdir(backup_dir_path)
    allfiles = list(filter(lambda file: file_name + backup_file_postfix in file and file_extension in file, allfiles))
    allfiles.sort()
    print(allfiles)
    for i in range(0, len(allfiles) - how_many_copies):
        os.remove(backup_dir_path + "\\" + allfiles[i])


# backup single file
def backup_file(file_path, back_up_dir_name, backup_file_postfix, how_many_copies=""):
    """
    Backup single file in a dedicated folder located in the file path.

    Args:
        file_path (path): single file path.
        back_up_dir_name (str): name of the dedicated folder.
        backup_file_postfix (str): postfix to the file name.
        how_many_copies (int): how many backup files to keep back.

    Returns:
        void: none

    """
    try:
        backup_dir_path = os.path.dirname(os.path.realpath(file_path)) + "\\" + back_up_dir_name
        if not (os.path.exists(backup_dir_path)):
            os.makedirs(backup_dir_path)
        file_name = Path(file_path).stem
        current_time = datetime.now().strftime("_%Y-%m-%d_%H-%M")
        file_extension = os.path.splitext(file_path)[1]

        backup_file_path = backup_dir_path + "\\" + file_name + backup_file_postfix + current_time + file_extension
        shutil.copy(file_path, backup_file_path)
        if how_many_copies:
            removing_extra_copies(backup_dir_path, file_name, backup_file_postfix, file_extension, how_many_copies)
    except:
        typer.echo("An error occurred (backup component)")


def backup_up_files(files, back_up_dir_name=CONST_BACKUP_DIR_NAME, backup_file_postfix=CONST_BACKUP_FILE_POSTFIX,
                    how_many_copies=""):
    """
    Backup each file in a dedicated folder located in the file path.

    Args:
        files (list(paths)): list of file paths.
        back_up_dir_name (str): name of the dedicated folder.
        backup_file_postfix (str): postfix to the file name.
        how_many_copies (int): how many backup files to keep back.

    Returns:
        void: none

    """
    for file in files:
        backup_file(file, back_up_dir_name, backup_file_postfix, how_many_copies)
