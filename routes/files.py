from __future__ import annotations
from routes.validation import validate_source_files
from routes.replacer import replace,find
import typer
from pathlib import Path
from typing import List
import os


app = typer.Typer()
# ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))


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
    Given a list of files, finds all associated files and replaces the target strings with the desired string.

    Args:
        src_files (list(path)): list of paths, source List of files that need to be change.
        find_file_path (path): Full path to the text file that contains the text to search for.
        replace_file_path (path): Full path to the text file that contains the text to insert instead of the text that was found.
        regular_expression_mode (bool): whether the text in file_to_find is a regex pattern or not.

    Returns:
        void: none
    """
    # Pre-processing
    validate_source_files(src_files)
    src_files = find(src_files, find_file_path=find_file_path, regular_expression_mode= regular_expression_mode)
    typer.echo("src files validation passed")
    # Process
    replace(src_files, find_file_path=find_file_path, replace_file_path= replace_file_path, regular_expression_mode= regular_expression_mode)
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
    Given a list of files, finds all files which according to the search input should make one or more substitutions.

    Args:
        src_files (path):  Full path to the directory that contains the text files that need to be change.
        find_file_path (path): Full path to the text file that contains the text to search for.
        regular_expression_mode (bool): whether the text in file_to_find is a regex pattern or not.

    Returns:
        void: none
    """

    # Pre-processing
    validate_source_files(src_files)
    typer.echo("src files validation passed")
    # Process
    list_of_paths = find(src_files, find_file_path=find_file_path, regular_expression_mode= regular_expression_mode)
    # Post-processing
    for path in list_of_paths:
        typer.echo(path)


