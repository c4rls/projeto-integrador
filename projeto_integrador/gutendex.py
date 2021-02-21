import requests
from book import Book, Author
from typing import List, Union

gutendex_url = 'http://gutendex.com'


def transform_results_into_books(results) -> List[Book]:
    books = []

    for result in results:
        authors = []
        for i in result['authors']:
            author = Author(
                i['name'], i['birth_year'], i['death_year'])
            authors.append(author)

        book = Book(result['id'], result['title'], authors, result['subjects'],
                    result['languages'], result['copyright'], result['formats'],
                    result['download_count'])

        books.append(book)

    return books


def get_books_by_ids(book_ids: Union[int, str]) -> List[Book]:
    ids = ','.join([str(x) for x in book_ids])
    url = gutendex_url + '/books?ids=' + ids
    books = []

    response = requests.get(url)

    if response.status_code == requests.codes.OK:
        data = response.json()
        results = data['results']

        books = transform_results_into_books(results)

    return books


def search_books(text: str) -> List[Book]:
    url = gutendex_url + '/books?search=' + text.lower().replace(' ', '%20')
    response = requests.get(url)
    books = []

    if response.status_code == requests.codes.OK:
        data = response.json()
        results = data['results']

        books = transform_results_into_books(results)

    return books
