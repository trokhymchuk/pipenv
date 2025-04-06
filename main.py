from app.io.input import input_builtin, input_console, input_pandas
from app.io.output import output_console, output_builtin


def main():
    output_console("Please, enter path to the input file: ")
    input_file_path = input_console()
    string_file_contents = input_builtin(input_file_path)
    pandas_file_contents = input_pandas(input_file_path)

    output_console(input_file_path)
    output_console(string_file_contents)
    output_console(pandas_file_contents.to_string())

    output_console("Please, enter path to the output file: ")
    output_file_path = input_console()
    output_builtin(input_file_path, output_file_path)
    output_builtin(string_file_contents, output_file_path)
    output_builtin(pandas_file_contents.to_string(), output_file_path)
    pass


if __name__ == '__main__':
    main()
