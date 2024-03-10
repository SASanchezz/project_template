import app.io.input as input
import app.io.output as output


def process_text_from_console():
    # Call function to input text from console
    return input.input_text_from_console()


def process_text_from_file():
    # Call function to read text from file using Python's built-in capabilities
    file_path = "data/example.txt"
    return input.read_text_from_file(file_path)


def process_text_from_pandas():
    # Call function to read text from file using pandas
    pandas_file_path = "data/example.csv"
    return input.read_text_from_file_with_pandas(pandas_file_path)


def output_text_to_console(text):
    # Output text to console
    output.output_text_to_console(text)


def write_text_to_file(text, file_name):
    # Write text to file using Python's built-in capabilities
    output.write_text_to_file(text, file_name)


def main():
    # Process text from console
    text_from_console = process_text_from_console()
    output_text_to_console(text_from_console)
    write_text_to_file(text_from_console, "data/output_console.txt")

    # Process text from file
    text_from_file = process_text_from_file()
    output_text_to_console(text_from_file)
    write_text_to_file(text_from_file, "data/output_file.txt")

    # Process text from pandas
    text_from_pandas = process_text_from_pandas()
    output_text_to_console(text_from_pandas)
    write_text_to_file(text_from_pandas, "data/output_pandas.txt")


if __name__ == "__main__":
    main()
