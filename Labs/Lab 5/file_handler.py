import enum
import json
import os


class FileExtensions(enum.Enum):
    TXT = 1
    JSON = 2


class FileHandler:

    @staticmethod
    def load_data(path, file_extension):
        try:
            with open(path, mode="r", encoding='utf-8') as text_file:
                if file_extension == FileExtensions.JSON:
                    data = json.loads(text_file.read())
                    return data
                elif file_extension == FileExtensions.TXT:
                    data = text_file.read()
                    return data

        except InvalidFileTypeError:
            print("invalid file type")

    @staticmethod
    def write_lines(path, lines):
        with open(path, "a") as file_object:
            file_object.write(lines + "\n")




class InvalidFileTypeError(Exception):
    def __init__(self):
        print("Invalid file type, please try again")
