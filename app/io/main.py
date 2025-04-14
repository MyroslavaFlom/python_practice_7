from input import input_from_console, input_from_file, input_from_pandas_file
from output import output_to_console, output_to_file
def main():
    text_console = input_from_console()
    text_file = input_from_file()
    df_pandas = input_from_pandas_file()

    output_to_console(text_console)
    output_to_console(text_file)
    output_to_console(df_pandas)

    output_to_file(text_console, 'output_console.txt')
    output_to_file(text_file, 'output_file.txt')
    output_to_file(df_pandas.to_string(), 'output_pandas.txt')


if __name__ == "__main__":
    main()