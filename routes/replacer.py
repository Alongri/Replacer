from __future__ import annotations
import routes.backup as backup
import routes.validation as validation
import regex as re
import typer
from routes.writer import write_file_content

from routes.reader import read_file_content


def find(src_files, find_file_path, regular_expression_mode):
    """
    Given a source strings, string or regex to find, replacement string, and regex mode, replaces all occurrences of the given string or regex matches in the source string with the replacement string.

    Args:
        src_files (list(path)): the replacement operation will be performed on these files.
        find_file_path (path): file path that contains a text file that is a string or regex pattern.
        regular_expression_mode (bool): whether the text in file_to_find is a regex pattern or not.

    Returns:
        str: The string after the replacements.

    """
    list_of_paths = []
    find_what = read_file_content(find_file_path)
    validation.validate_regex_expression(find_what)

    for i in range(0, len(src_files)):
        src_content = read_file_content(src_files[i])
        if regular_expression_mode:
            if len(re.findall(find_what, src_content)) > 0:
                list_of_paths.append(src_content[i])
        else:
            if find_what in src_content:
                list_of_paths.append(src_content[i])

    return list_of_paths


def replace_string(source_string, replace_with, regex):
    """
    Given a source string, regex pattern, replacement string, replaces all occurrences of the regex matches in the source string with the replacement string.

    Args:
        source_string (str): the string on which the replacement will be performed.
        replace_with (str): the string to be replaced.
        regex (str): regex pattern.

    Returns:
        str: The string after the replacements.

    """

    shift = 0
    for elem in [(m.start(),m.end()) for m in re.finditer(regex, source_string)]:
        source_string = source_string[: elem[0] + shift] + replace_with + source_string[elem[1] + shift:]
        shift += len(replace_with) - (elem[1] - elem[0])
    return source_string


def replace(src_files, find_file_path, replace_file_path, regular_expression_mode):
    """
    Given a source strings, string or regex to find, replacement string, and regex mode, replaces all occurrences of the given string or regex matches in the source string with the replacement string.

    Args:
        src_files (list(path)): the replacement operation will be performed on these files.
        find_file_path (path): file path that contains a text file that is a string or regex pattern.
        replace_file_path (path): file path that contains a text file that is a  string to be replaced.
        regular_expression_mode (bool): whether the text in file_to_find is a regex pattern or not.

    Returns:
        str: The string after the replacements
    """
    try:
        # Files backup
        backup.backup_up_files(src_files)

        find_what = read_file_content(find_file_path)
        replace_with = read_file_content(replace_file_path)
        validation.validate_regex_expression(find_what)

        for i in range(0, len(src_files)):
            src_content = read_file_content(src_files[i])
            if regular_expression_mode:
                src_content = replace_string(src_content, replace_with, find_what)
            else:
                src_content = src_content.replace(find_what, replace_with)

            write_file_content(src_files[i], src_content)

        typer.echo("Action passed!")
    except:
        typer.echo("An error occurred (replacer component)")


if __name__ == '__main__':
    print(replace_string("abbbabbbabbb", "aa", "a|bbb"))