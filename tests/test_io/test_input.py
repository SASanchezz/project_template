import pytest
import app.io.input as my_input


# Test cases for reading text from a file using Python's built-in capabilities
def test_read_text_from_file_exists():
    # Ensure that the function exists
    assert callable(my_input.read_text_from_file)


def test_read_text_from_file_returns_string():
    # Ensure that the function returns a string
    file_path = "data/example.txt"  # File must exist
    assert isinstance(my_input.read_text_from_file(file_path), str)


def test_read_text_from_file_with_invalid_file():
    # Ensure that the function raises FileNotFoundError for invalid file path
    with pytest.raises(FileNotFoundError):
        my_input.read_text_from_file("nonexistent_file.txt")


# Test cases for reading text from a file using pandas
def test_read_text_from_file_with_pandas_exists():
    # Ensure that the function exists
    assert callable(my_input.read_text_from_file_with_pandas)


def test_read_text_from_file_with_pandas_returns_string():
    # Ensure that the function returns a string
    pandas_file_path = "data/example.csv"
    assert isinstance(my_input.read_text_from_file_with_pandas(pandas_file_path), str)


def test_read_text_from_file_with_pandas_with_invalid_file():
    # Ensure that the function raises FileNotFoundError for invalid file path
    with pytest.raises(FileNotFoundError):
        my_input.read_text_from_file_with_pandas("nonexistent_file.csv")
