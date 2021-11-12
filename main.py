from bs4 import BeautifulSoup
import os
import pprint

class PathFinder:
    @staticmethod
    def get_filenames(directory):
        return next(os.walk(directory), (None, None, []))[2]


class HTMLReader(PathFinder):

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


class InformationExtractor(HTMLReader):
    def get_artist_names(self, directory):
        files = self.get_files(directory)
        artist_names = []
        for file in files:
            artist_names.append(self.get_artist_name(file))
        return artist_names

    def artist_dict_builder(self, directory):

        artist_names = self.get_artist_names(directory=directory)
        artists_works_list = []

        for artist in artist_names:
            artists_dict = {}
            artists_dict['artist'] = artist
            artists_dict['works'] = self.get_works_of_an_artist(artist=artist, directory=directory)
            artists_works_list.append(artists_dict)

        print(artists_works_list)




    @staticmethod
    def get_artist_name(file):
        return file.h2.text

    @staticmethod
    def get_work_name(file):
        return file.h3.text

    @staticmethod
    def get_work_sale(file):
        return file.findAll('div')[1].text

    @staticmethod
    def split_price_and_currency(sale_string):
        return sale_string.split(" ")

    def get_works_of_an_artist(self, artist, directory):
        files = self.get_files(directory)
        work_names = []
        for file in files:
            if artist == self.get_artist_name(file):
                work_names.append(self.get_work_name(file))

        return work_names


if __name__ == '__main__':
    parser_class = InformationExtractor()

    path = 'data/2015-03-18/'
    #print(parser_class.get_works_of_an_artist('Rembrandt Harmensz. van Rijn', path))

    pprint.pprint(parser_class.artist_dict_builder(path))
