from typing import List, Union
from ebooklib.epub import Link, Section
from bs4 import BeautifulSoup, Tag, NavigableString, Comment
from typography import Title, Paragraph, TypographyList


disallowed_tags = ['[document]', 'noscript', 'header', 'html',
                   'meta', 'head', 'input', 'script', 'style'
                   'img', 'iframe', 'textarea', 'button', 'select',
                   'canvas', 'svg']
title_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
text_tags = ['p']


def get_links_from_toc(toc: List[Union[Link, Section]]) -> List[Link]:
    links = []

    def func(x):
        if isinstance(x, Link):
            links.append(x)
        elif isinstance(x, Section):
            links.append(Link(x.href, x.title))
        elif isinstance(x, (tuple, list)):
            for i in x:
                func(i)

    for item in toc:
        func(item)

    return links


def get_page_content(file_content, start_identifier, end_identifier) -> List[Union[Tag, NavigableString]]:
    soup = BeautifulSoup(file_content, 'html.parser')
    start = None
    end = None

    if not start_identifier:
        raise Exception()

    start = soup.body.find(attrs={'id': start_identifier})
    if not start:
        raise Exception()

    if end_identifier:
        end = soup.body.find(attrs={'id': end_identifier})

    def clean(first_element, mode):
        if mode != 'up' and mode != 'down':
            raise Exception()

        current = first_element
        while current != soup.body.parent:
            parent = current.parent

            index_current = parent.contents.index(current)

            if mode == 'up':
                del(parent.contents[:index_current])
            else:
                if current == first_element:
                    del(parent.contents[index_current:])
                else:
                    del(parent.contents[index_current + 1:])

            current = parent

    clean(start, 'up')

    if end:
        clean(end, 'down')

    return soup.body.contents


def parse_content(content: List[Union[Tag, NavigableString]]) -> TypographyList:
    text_list = []

    def func(x):
        if isinstance(x, Comment):
            pass
        elif isinstance(x, NavigableString):
            text = x.strip()
            if text:
                text_list.append(Paragraph(text=text))
        elif isinstance(x, Tag):
            if x.name in title_tags:
                text = x.get_text().strip()
                if text:
                    text_list.append(Title(text=text))
            elif x.name in text_tags:
                text = x.get_text().strip()
                if text:
                    text_list.append(Paragraph(text=text))
            elif x.name in disallowed_tags:
                pass
            else:
                for i in x.contents:
                    func(i)

    for item in content:
        func(item)

    return TypographyList(text_list)
