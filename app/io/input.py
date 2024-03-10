def input_text_from_console():
    """
    Function to input text from the console.

    Returns:
        str: The text entered from the console.
    """
    text = input("Enter text: ")
    return text


def read_text_from_file(file_path):
    """
    Function to read text from a file using Python's built-in capabilities.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The read text from the file.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def read_text_from_file_with_pandas(file_path):
    """
    Function to read text from a file using the pandas library.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The read text from the file.
    """
    import pandas as pd
    data = pd.read_csv(file_path)
    text = data.to_string(index=False, header=False)
    return text
