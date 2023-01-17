def write_file_content(file_path, content):
    """
    Write into a text file.

    Args:
        file_path (path): text file path.
        content (str): the content to be written to the text file.

    Returns:
        void: none

    """
    with open(file_path, 'w', encoding='utf-8') as file_path_content:
        file_path_content.write(content)