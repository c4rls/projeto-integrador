from kivy.app import App
import requests
from typing import List, Union
import os


class Author:

    def __init__(self, name, birth_year, death_year):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year


class Book:

    def __init__(
            self,
            id,
            title,
            authors: List[Author],
            subjects: List[str],
            languages: List[str],
            copyright: Union[bool, None],
            formats: dict,
            download_count):
        self.id = str(id)
        self.title = title
        self.authors = authors
        self.subjects = subjects
        self.languages = languages
        self.copyright = copyright
        self.formats = formats
        self.download_count = download_count

    def to_string(self):
        return f'<Book (Id: {self.id}, Title: {self.title})>'

    def to_full_string(self):
        return f'''<Book (
    Id: {self.id},
    Title: {self.title},
    Authors: {' - '.join([x.name for x in self.authors])},
    Public Domain: {'yes' if not self.copyright else 'no'},
    EPUB Download: {'yes' if self.epub_is_avaliable() else 'no'})>'''

    def epub_is_avaliable(self) -> bool:
        epub_formats = ['application/epub+zip']
        formats = self.formats.keys()

        for i in epub_formats:
            if i in formats:
                return True

        return False

    def epub_download(self):
        if not self.epub_is_avaliable():
            print(
                f'O livro ({self.title}) não está disponível para download no formato epub')
            return

        app = App.get_running_app()

        files = os.listdir(app.user_data_dir)
        if 'epub_downloads' not in files:
            os.mkdir(app.user_data_dir + '/epub_downloads')

        file_path = app.user_data_dir + '/epub_downloads/' + self.id + '.epub'

        print('Fazendo o download do livro ' + self.to_string())
        response = requests.get(self.formats['application/epub+zip'])

        if response.status_code == requests.codes.OK:
            with open(file_path, 'wb') as file:
                file.write(response.content)

            print('Download finalizado. O arquivo está disponível em: ' + file_path)
        else:
            print('Erro ao fazer o download')

    def epub_remove(self):
        app = App.get_running_app()

        files = os.listdir(app.user_data_dir)
        if 'epub_downloads' in files:
            file_name = self.id + '.epub'
            if file_name in os.listdir(app.user_data_dir + '/epub_downloads'):
                print('Removendo o livro ' + self.to_string())
                os.remove(app.user_data_dir + '/epub_downloads/' + file_name)
                print('O livro ' + self.to_string() + ' foi removido')
