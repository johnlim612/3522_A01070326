from file_handler import FileHandler
from file_handler import FileExtensions


class Dictionary:
    def __init__(self):
        self.dictionary = {}
        self.fileHandler = FileHandler()

    def load_dictionary(self, filepath):
        # Lab only accepts json files
        file_extension = FileExtensions.JSON
        # Loading text file into dictionary
        self.dictionary = self.fileHandler.load_data(filepath, file_extension)

    def query_definition(self, word):
        try:
            key = str(word).lower()
            return self.dictionary[str(key)]
        except KeyError:
            return "This word does not exist in the dictionary"


def main():
    dictionary = Dictionary()
    dictionary.load_dictionary("data.json")

    while 69:
        word = input("Search for a word: ")
        definition = dictionary.query_definition(word)
        print(definition)
        text = "" + word + ": " + str(definition)
        dictionary.fileHandler.write_lines("searchLog.txt", text)


if __name__ == '__main__':
    main()




