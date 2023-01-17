from __future__ import annotations

import regex as re
import typer
import os.path
from com import FILE_ERROR, ERRORS, REGEX_ERROR


# ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

def validate_source_files(src_files):
    """
    Checks if the given list is valid input for the replacer.

    Args:
        src_files (list(path)): list of text paths.

    Returns:
        void: none
    """
    validate_source_files_existence(src_files)
    validate_if_file_in_source_files_is_file(src_files)
    validate_if_file_not_readable(src_files)
    validate_if_file_not_writable(src_files)


def validate_source_files_existence(src_files):
    """
    Checks if every path is valid and exist.

    Args:
        src_files (list(path)): list of text paths.

    Returns:
        void: none
    """
    # If one of the sources is not exists
    for path in src_files:
        if os.path.exists(path):
            pass
        else:
            typer.echo(f"This file does not exists")
            typer.echo(ERRORS.get(FILE_ERROR))
            raise typer.Exit(FILE_ERROR)


def validate_if_file_in_source_files_is_file(src_files):
    """
    Checks if every file is valid file.

    Args:
        src_files (list(path)): list of text paths.

    Returns:
        void: none
    """

    # check if file in src_files is not a file
    for path in src_files:
        if path.is_file():
            pass
        else:
            typer.echo(f"This file not exists: {path.name}")
            typer.echo(ERRORS.get(FILE_ERROR))
            raise typer.Exit(FILE_ERROR)


def validate_if_file_not_readable(src_files):
    """
    Checks if every file is readable file.

    Args:
        src_files (list(path)): list of text paths.

    Returns:
        void: none
    """

    for path in src_files:
        if os.access(path, os.R_OK):
            pass
        else:
            typer.echo(f"This file is not readable: {path.name}")
            typer.echo(ERRORS.get(FILE_ERROR))
            raise typer.Exit(FILE_ERROR)


def validate_if_file_not_writable(src_files):
    """
    Checks if every file is writable file.

    Args:
        src_files (list(path)): list of text paths

    Returns:
        void: none
    """
    for path in src_files:
        if os.access(path, os.R_OK):
            pass
        else:
            typer.echo(f"This file is not writable: {path.name}")
            typer.echo(ERRORS.get(FILE_ERROR))
            raise typer.Exit(FILE_ERROR)


def validate_regex_expression(regex_expression):
    """
    Checks if given string is valid regex pattern.

    Args:
        regex_expression (str): regex pattern.

    Returns:
        void: none
    """
    try:
        re.compile(regex_expression)
    except re.error:
        typer.echo(re.error)
        raise typer.Exit(REGEX_ERROR)


