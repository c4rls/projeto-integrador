from gutendex import search_books
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import kivy
kivy.require('1.11.1')

__version__ = '0.0.1'


class ScreenRoot(BoxLayout):
    search_box = ObjectProperty(None)
    books_list = ObjectProperty(None)

    def getBooks(self):
        terms = self.search_box.ids.search_input.text.strip()
        if not terms:
            return

        self.books_list.ids.books_list.clear_widgets()
        books = search_books(terms)

        for book in books:
            authors = ' - '.join([x.name for x in book.authors])
            link = book.formats['application/epub+zip'] if book.epub_is_avaliable(
            ) else 'Não disponível'

            book_widget = Book(title=book.title, authors=authors, link=link)
            self.books_list.ids.books_list.add_widget(book_widget)

        self.search_box.ids.search_input.text = ''
        self.books_list.ids.books_header.found_books = len(books)


class Book(BoxLayout):
    def __init__(self, title='', authors='', link='', **kwargs):
        super().__init__(**kwargs)
        self.title_content = title
        self.authors_content = authors
        self.link_content = link


class ProjetoIntegradorApp(App):
    def build(self):
        return ScreenRoot()


if __name__ == '__main__':
    ProjetoIntegradorApp().run()
