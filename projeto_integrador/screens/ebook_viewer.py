from threading import Thread, Event
from ebooklib.epub import read_epub
from kivy.app import App
from kivy.clock import mainthread, Clock
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel, MDIcon
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from typography import Title, Paragraph, Page, TypographyList
from utils import get_links_from_toc, get_page_content, parse_content
from widget_allocator import WidgetAllocator

Builder.load_file('screens/ebook_viewer.kv')


class EBookViewer(Screen):
    current_page = NumericProperty(1)
    max_page = NumericProperty(1)

    def __init__(self, **kwargs):
        super(EBookViewer, self).__init__(**kwargs)
        self._previous_screen = ''
        self._pages = []
        self._widget_allocator = WidgetAllocator(config=[
            ('title', EBookViewerTitle, 5, 10),
            ('paragraph', EBookViewerParagraph, 15, 30),
            ('separator', EBookViewerSeparator, 15, 30)])
        self._stop_event = Event()

    def stop(self):
        self._stop_event.set()
        self._widget_allocator.stop_allocation()

    def set_book(self, book):
        self._book = book

    def get_pages(self):
        self._pages = []

        app = App.get_running_app()

        book_file = read_epub(app.user_data_dir +
                              '/epub_downloads/' + self._book.id + '.epub')
        links = get_links_from_toc(book_file.toc)

        for i in range(0, len(links)):
            self._pages.append([None, Event()])

        self.current_page = 1
        self.max_page = len(links)

        def thread_func():
            for index, link in enumerate(links):
                if self._stop_event.is_set():
                    return

                file_name, start_identifier = link.href.split('#')

                next_file_name, end_identifier = links[index + 1].href.split(
                    '#') if index + 1 < len(links) else [None, None]

                content = book_file.get_item_with_href(file_name).get_content()
                page_content = None

                if next_file_name == file_name:
                    page_content = get_page_content(
                        content, start_identifier, end_identifier)
                else:
                    page_content = get_page_content(
                        content, start_identifier, None)

                parsed_content = parse_content(page_content)

                page = Page(parsed_content)
                self._add_page(page, index)

        Thread(target=thread_func).start()

    @ mainthread
    def _add_page(self, page, index):
        value = self._pages[index]
        value[0] = EBookViewerPage(
            page=page, widget_allocator=self._widget_allocator)
        value[1].set()

    def show_page(self, index):
        if not self._widget_allocator.allocation_is_active():
            self._widget_allocator.start_allocation()

        container = self.ids.container
        container.clear_widgets()

        page, page_created_event = self._pages[index]

        if page:
            container.add_widget(page)
            if not page.is_rendered():
                Thread(target=page.render).start()

            return

        def thread_func():
            while not page_created_event.is_set():
                if self._stop_event.is_set():
                    return

            x()

        @mainthread
        def x():
            page = self._pages[index][0]

            container.add_widget(page)
            if not page.is_rendered():
                Thread(target=page.render).start()

        Thread(target=thread_func).start()

    def set_previous_screen(self, previous_screen):
        self._previous_screen = previous_screen

    def _go_to_previous_screen(self):
        app = App.get_running_app()

        self._widget_allocator.stop_allocation()

        app.root.current = self._previous_screen if self._previous_screen else 'home'

    def _go_to_next_page(self):
        self.current_page = self.current_page if self.current_page == self.max_page else self.current_page + 1
        self.show_page(self.current_page - 1)

    def _go_to_previous_page(self):
        self.current_page = 1 if self.current_page == 1 else self.current_page - 1
        self.show_page(self.current_page - 1)


class EBookViewerPage(BoxLayout):
    def __init__(self, page=None, widget_allocator=None, **kwargs):
        super(EBookViewerPage, self).__init__(**kwargs)
        self._page = page
        self._rendered = False
        self._widget_allocator = widget_allocator

    def get_page(self):
        return self._page

    def is_rendered(self):
        return self._rendered

    @mainthread
    def _render_component(self, component):
        container = self.ids.container

        if isinstance(component, Title):
            title = self._widget_allocator.get_widget('title')
            separator = self._widget_allocator.get_widget('separator')
            title.text = component.text
            separator.multiplier = 3
            container.add_widget(title)
            container.add_widget(separator)
        elif isinstance(component, Paragraph):
            paragraph = self._widget_allocator.get_widget('paragraph')
            separator = self._widget_allocator.get_widget('separator')
            paragraph.text = component.text
            separator.multiplier = 2
            container.add_widget(paragraph)
            container.add_widget(separator)

    def render(self):
        Clock.schedule_once(lambda _: self.ids.container.clear_widgets(), 0)

        for i in self._page.content.text_list:
            self._render_component(i)

        self._rendered = True


class EBookViewerTitle(MDLabel):
    def __init__(self, text='', **kwargs):
        super(EBookViewerTitle, self).__init__(**kwargs)
        self.text = text


class EBookViewerParagraph(MDLabel):
    def __init__(self, text='', **kwargs):
        super(EBookViewerParagraph, self).__init__(**kwargs)
        self.text = text


class EBookViewerSeparator(Widget):
    multiplier = NumericProperty(1)

    def __init__(self, multiplier=1, **kwargs):
        super(EBookViewerSeparator, self).__init__(**kwargs)
        self.multiplier = multiplier
