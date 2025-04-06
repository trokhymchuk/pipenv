import pandas

def input_console():
    """
    Return input from user from console.
    Return:
        str. text, entered by the user.
    """
    return input()


def input_builtin(file_path):
    """
    Return contents of the file using builtin functions.
    Args:
        file_path(str): path to the file to be read.
    Return:
        str: contents of the file.
    """
    return open(file_path, encoding='utf-8').read()


def input_pandas(file_path, format = 'csv'):
    """
    Return contents of the file, parsed, using pandsas.
    Args:
        file_path(str): The path to the file to be read.
        format(str): format of the input file, csv and json are supported.
    Returns:
        df(pandas.DataFrame): contents of the file, parsed.
    Throws:
       ValueError: if format is unsupported
    """
    if format == 'csv':
        return pandas.read_csv(file_path)
    elif format == 'json':
        return pandas.read_json(file_path)
    else:
        raise ValueError(f"Format '{format}' is not suported")