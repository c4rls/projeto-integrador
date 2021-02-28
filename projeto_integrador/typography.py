from __future__ import annotations
from typing import Union, List


class Text:
    def __init__(self, text=''):
        self.text = text


class Title(Text):
    pass


class Paragraph(Text):
    pass


class TypographyList:
    def __init__(self, text_list: List[Union[Title, Paragraph]]):
        self.text_list = text_list

    def get_chunk(self, start=0, end=0) -> TypographyList:

        return TypographyList(text_list=self.text_list[start:end + 1])


class Page:
    def __init__(self, content: TypographyList):
        self.content = content
