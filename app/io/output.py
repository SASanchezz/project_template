def output_text_to_console(text):
    """
    Function to output text to the console.

    Args:
        text (str): The text to be printed.
    """
    print(text)


def write_text_to_file(text, file_path):
    """
    Function to write text to a file.

    Args:
        text (str): The text to be written.
        file_path (str): The path to the file.
    """
    with open(file_path, 'w') as file:
        file.write(text)
