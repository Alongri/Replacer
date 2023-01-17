from __future__ import annotations
import routes.files as files
import typer
from pathlib import Path
import os


app = typer.Typer()
# ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))


def absoluteFilePaths(directory):
    """
    Creates a list of files located in the given folder path.

    Args:
        directory (path): Full path to the directory that contains the text files that need to be changes.

    Returns:
        list(path)

    """
    path_list = []
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            path_list.append(Path(os.path.abspath(os.path.join(dirpath, f))))
    return path_list


@app.command()
def find_and_replace(s_dir: Path = typer.Option(..., exists=True, file_okay=False, dir_okay=True,
                                                writable=False, readable=True, resolve_path=True,
                                                help="Full path to the directory that contains "
                                                     "the text files that need to be changes"),

                     find_file_path: Path = typer.Option(..., exists=True, file_okay=True, dir_okay=False,
                                                    writable=False, readable=True, resolve_path=True,
                                                    help="Full path to the text file that contains "
                                                         "the text to search for (supports regular expression if "
                                                         "regular_expression_mode is on)"),

                     replace_file_path: Path = typer.Option(..., exists=True, file_okay=True, dir_okay=False,
                                                       writable=False, readable=True, resolve_path=True,
                                                       help="Full path to the text file that contains "
                                                            "the text to insert instead of the text that was "
                                                            "found"),
                     regular_expression_mode: bool = True):
    """
    Given a directory, takes all the files in the directory and finds all associated files and replaces the target strings with the desired string.

    Args:
        s_dir (path):  Full path to the directory that contains the text files that need to be change.
        find_file_path (path): Full path to the text file that contains the text to search for.
        replace_file_path (path): Full path to the text file that contains the text to insert instead of the text that was found.
        regular_expression_mode (bool): whether the text in file_to_find is a regex pattern or not.

    Returns:
        void: none
    """
    # Pre-processing
    path_list = absoluteFilePaths(s_dir)
    typer.echo("dir pre-processing passed")
    # Process
    files.find_and_replace_files(path_list, find_file_path=find_file_path, replace_file_path=replace_file_path, regular_expression_mode=regular_expression_mode)
    # Post-processing


@app.command()
def find_files(s_dir: Path = typer.Option(..., exists=True, file_okay=False, dir_okay=True,
                                                writable=False, readable=True, resolve_path=True,
                                                help="Full path to the directory that contains "
                                                     "the text files that need to be changes"),

                     find_file_path: Path = typer.Option(..., exists=True, file_okay=True, dir_okay=False,
                                                    writable=False, readable=True, resolve_path=True,
                                                    help="Full path to the text file that contains "
                                                         "the text to search for (supports regular expression if "
                                                         "regular_expression_mode is on)"),

                     regular_expression_mode: bool = True):
    """
    Given a directory, takes all the files in the directory and finds all files which according to the search input should make one or more substitutions.

    Args:
        s_dir (path):  Full path to the directory that contains the text files that need to be change.
        find_file_path (path): Full path to the text file that contains the text to search for.
        regular_expression_mode (bool): whether the text in file_to_find is a regex pattern or not.

    Returns:
        void: none
    """
    # Pre-processing
    path_list = absoluteFilePaths(s_dir)
    typer.echo("dir pre-processing passed")
    # Process
    files.find_files(path_list, find_file_path=find_file_path , regular_expression_mode=regular_expression_mode)
    # Post-processing

