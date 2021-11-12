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

            total_sales = self.calculate_total_sales(
                self.get_works_of_an_artist(
                    artist=artist,
                    directory=directory
                )
            )
            artists_dict = {
                'artist': artist,
                'totalValue': 'USD ' + str(total_sales),
                'works': self.get_works_of_an_artist(artist=artist, directory=directory)
            }
            artists_works_list.append(artists_dict)

        return artists_works_list

    @staticmethod
    def calculate_total_sales(works):
        total_sale = 0
        for work in works:
            if work['currency'] == 'USD':
                total_sale += int(work['amount'].replace(',', ''))
            else:
                total_sale += int(work['amount'].replace(',', '')) * 1.35

        return total_sale




    def get_artist_name(self, file):
        if self.is_fine_new_type(file):
            return file.h3.text
        else:
            return file.h3.text

    @staticmethod
    def get_work_name(file):
        return file.h3.text

    def get_work_sale(self, file):
        if self.is_fine_new_type(file):
            return self.get_currency_span(file)[0].text + ' ' + self.get_currency_span(file)[1].text
        else:
            return file.findAll('div')[1].text
            file.find(id="currency")

    @staticmethod
    def get_currency_span(file):
        return file.findAll('div')[1].findAll('span')

    @staticmethod
    def is_fine_new_type(file):
        if file.h3.text.find("class"):
            return True
        else:
            return False

    @staticmethod
    def split_price_and_currency(sale_string):
        return sale_string.split(" ")

    def get_works_of_an_artist(self, artist, directory):
        files = self.get_files(directory)
        works = []
        for file in files:
            if artist == self.get_artist_name(file):
                work_dict = {
                    'title': self.get_work_name(file),
                    'currency': self.split_price_and_currency(self.get_work_sale(file))[0],
                    'amount': self.split_price_and_currency(self.get_work_sale(file))[1]
                }
                works.append(work_dict)

        return works


if __name__ == '__main__':
    parser_class = InformationExtractor()

    path = 'data/2017-12-20/'
    pprint.pprint(parser_class.artist_dict_builder(path))
