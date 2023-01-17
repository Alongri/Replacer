def read_file_content(find_file_path):
    """
    Reads a text file.

    Args:
        find_file_path (path): text file path.

    Returns:
        str: the content of the text file.

    """
    text = []
    with open(find_file_path, 'r', encoding='utf-8') as src_file_path:
        text = src_file_path.read()
    return "".join(text)
