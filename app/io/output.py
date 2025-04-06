def output_console(text):
    """
    Print text to the console.
    Args:
        text (str): text to display to print in console.
    """
    print(text)


def output_builtin(text, file_path):
    """
    Print text to file using built-in functions.
    Args:
        text (str): text to display to print in console.
        file_path(str): The path to the file to output to.
    """
    open(file_path, 'w', encoding='utf-8').write(text)
