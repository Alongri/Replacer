from __future__ import annotations
from routes.reader import read_file_content

import routes.files as files
import typer
from typing import List
import regex as re
import os
import os.path
from pathlib import Path

app = typer.Typer()
# ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
CONST_REGEX_PATH = r"path=\"(.*?)\""
CONST_REGEX_FILE = r"file=\"(.*?)\""


def find_related_files(file):
    """
    Finds campaigns, test-cases and procedures paths mentioned in the text file itself.

    Args:
        file(path)

    Returns:
        list(path)

    """
    file_content = read_file_content(file)
    founds = set(re.findall(CONST_REGEX_FILE, file_content))
    founds.update(set(re.findall(CONST_REGEX_PATH, file_content)))
    return founds


def search_deeper(single_file):
    """
    Recursive method, finds all associated campaigns, test-cases and procedures of single file.

    Args:
        single_file(path)

    Returns:
        list(path)

    """
    related_files = find_related_files(single_file)
    for file in related_files.copy():
        file_extension = os.path.splitext(file)[1]
        if "atc" in file_extension or "attc" in file_extension:
            related_files.update(search_deeper(file))
    return related_files


def set_to_list_of_paths(my_set):
    """
    Create list of path from given set.

    Args:
        my_set (set(path))

    Returns:
        list(path)

    """
    my_list = []
    for path in my_set:
        my_list.append(Path(path))
    return my_list


def deeper(src_files):
    """
    Search deeper and finds all associated campaigns, test-cases and procedures.

    Args:
        src_files (list(path))

    Returns:
        list(path)
    """
    try:
        files_set = set(src_files)
        for file in src_files:
            files_set.update(search_deeper(file))
        return set_to_list_of_paths(files_set)
    except:
        typer.echo(f"An error occurred (deeper component)")
        raise typer.Exit()


@app.command()
def find_and_replace_files(src_files: List[Path] = typer.Option(...,
                                                                help=" Source List of files that need to be change. "),

                           find_file_path: Path = typer.Option(..., exists=True, file_okay=True, dir_okay=False,
                                                               writable=False, readable=True, resolve_path=True,
                                                               help="Full path to the text file that contains "
                                                                    "the text to search for (supports regular "
                                                                    "expression if "
                                                                    "regular_expression_mode is on)", prompt=True),

                           replace_file_path: Path = typer.Option(..., exists=True, file_okay=True, dir_okay=False,
                                                                  writable=False, readable=True, resolve_path=True,
                                                                  help="Full path to the text file that contains "
                                                                       "the text to insert instead of the text that "
                                                                       "was "
                                                                       "found", prompt=True),

                           regular_expression_mode: bool = typer.Option(True, "--regexMode")):
    """
    Given a list of files, search deeper and finds all associated files and replaces the target strings with the desired string.

    Args:
        src_files (list(path)): source List of files that need to be change
        find_file_path (path): Full path to the text file that contains the text to search for
        replace_file_path (path): Full path to the text file that contains the text to insert instead of the text that was found
        regular_expression_mode (bool): whether the text in file_to_find is a regex pattern or not.

    Returns:
        void: none
    """
    # Pre-processing
    src_files = deeper(src_files)
    typer.echo("Deeper pre-processing passed")
    # Process
    files.find_and_replace_files(src_files, find_file_path=find_file_path, replace_file_path=replace_file_path,
                                 regular_expression_mode=regular_expression_mode)
    # Post-processing


@app.command()
def find_files(src_files: List[Path] = typer.Option(...,
                                                    help=" Source List of files that need to be change. "),

               find_file_path: Path = typer.Option(..., exists=True, file_okay=True, dir_okay=False,
                                                   writable=False, readable=True, resolve_path=True,
                                                   help="Full path to the text file that contains "
                                                        "the text to search for (supports regular "
                                                        "expression if "
                                                        "regular_expression_mode is on)", prompt=True),

               regular_expression_mode: bool = typer.Option(True, "--regexMode")):
    """
    Given a list of files, search deeper and finds all associated files which according to the search input should make one or more substitutions.

    Args:
        src_files (list(path)): source List of files that need to be change.
        find_file_path (path): Full path to the text file that contains the text to search for.
        regular_expression_mode (bool): whether the text in file_to_find is a regex pattern or not.

    Returns:
        void: none
    """
    # Pre-processing
    src_files = deeper(src_files)
    typer.echo("Deeper pre-processing passed")
    # Process
    files.find_files(src_files, find_file_path=find_file_path, regular_expression_mode=regular_expression_mode)
    # Post-processing


if __name__ == '__main__':
    list = []
    list.append(r"C:\QA\AutoTester_Campaigns\idan.atc")
    print("gg")
