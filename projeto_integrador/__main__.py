from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import kivy
kivy.require('1.11.1')


class ScreenRoot(BoxLayout):
    search_box = ObjectProperty(None)
    books_list = ObjectProperty(None)

    def getBooks(self):
        books = []
        terms = self.search_box.ids.search_input.text.strip()
        if not terms:
            return

        self.books_list.ids.books_list.clear_widgets()
        for i in range(5):
            book = Book(title='Quincas Borba', authors='Machado de Assis',
                        link='https://link.com/ldi92kleh')

            books.append(book)

        for book in books:
            self.books_list.ids.books_list.add_widget(book)

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
