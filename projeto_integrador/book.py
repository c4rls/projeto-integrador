import requests
from typing import List, Union


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

    def epub_is_avaliable(self) -> bool:
        epub_formats = ['application/epub+zip']
        formats = self.formats.keys()

        for i in epub_formats:
            if i in formats:
                return True

        return False
