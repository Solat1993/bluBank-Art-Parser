from bs4 import BeautifulSoup
import os


class PathFinder:
    @staticmethod
    def get_filenames(directory):
        return next(os.walk(directory), (None, None, []))[2]


class HTMLReader(PathFinder):
    def __init__(self):
        pass

    @staticmethod
    def open_file(path):
        with open(path, 'r') as file:
            contents = file.read()

            return BeautifulSoup(contents, features="html.parser")

    def get_files(self, directory):
        file_names = self.get_filenames(directory)
        files = []
        for file_name in file_names:
            files.append(self.open_file(directory + file_name))

        return files


class InformationGetter(HTMLReader):
    def get_artist_name(self, directory):
        files = self.get_files(directory)
        artist_names = []
        for file in files:
            artist_names.append(file.h2.text)
        return artist_names


if __name__ == '__main__':
    parser_class = InformationGetter()

    path = 'data/2015-03-18/'
    print(parser_class.get_artist_name(path))
