from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivy.uix.behaviors import ButtonBehavior


Builder.load_file('components/book_card.kv')


class BookCard(MDCard):
    title_content = StringProperty('')

    def __init__(self, book=None, **kwargs):
        super(BookCard, self).__init__(**kwargs)
        self.title_content = book.title
        self.is_opened = False
        self.book = book

    def open_or_close_card(self):
        if self.is_opened:
            self.ids.content.clear_widgets()
            self.is_opened = False
            return

        self.is_opened = True
        card_content = BookCardContent()

        card_content.ids.info.add_widget(
            MDLabel(text='Autores: ' + ' - '.join([x.name for x in self.book.authors])))
        card_content.ids.info.add_widget(
            MDLabel(text='Download em ePUB: ' + 'Sim' if self.book.epub_is_avaliable() else 'Não'))

        card_content.ids.actions.add_widget(
            BookCardActionButton(text='Ler', on_release=lambda pos=None: self.read_book()))
        card_content.ids.actions.add_widget(
            BookCardActionButton(text='Baixar', on_release=lambda pos=None: self.download_book()))
        card_content.ids.actions.add_widget(
            BookCardActionButton(text='Remover', on_release=lambda pos=None: self.remove_book()))

        self.ids.content.add_widget(card_content)

    def download_book(self):
        self.book.epub_download()

    def remove_book(self):
        self.book.epub_remove()

    def read_book(self):
        pass


class BookCardContent(BoxLayout):
    pass


class BookCardActionButton(MDFlatButton):
    def __init__(self, md_bg_color=(0, 0.38, 0.35, 1), **kwargs):
        super(BookCardActionButton, self).__init__(**kwargs)
        self.md_bg_color = md_bg_color
