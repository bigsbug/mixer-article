import random
from typing import List
import re


class Article:
    def __init__(self, text: str, iterator: int) -> None:
        self.text = text
        self.iterator = iterator
        self.text_list = []
        self.convert_to_list()
        self.index = 0
        self.next_index = iterator
        self.limit = self.len()

    def convert_to_list(self) -> None:
        self.text = self.text.replace("_", " ")
        self.text_list = re.findall(r"[\w]+", self.text)

    def len(self):
        return self.text_list.__len__()

    def matching(self, length: int) -> None:
        for i in range(self.text_list.__len__(), length):
            self.text_list.append(random.choice(self.text_list))

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit > 0:
            if self.limit > (self.iterator - 1):
                result = self.text_list[self.index : self.next_index]
                self.index = self.next_index
                self.next_index += self.iterator
                self.limit -= self.iterator - 1
            else:
                self.limit = 0
                result = self.text_list[self.index : :]

            if result == []:
                raise StopIteration
            return result

        raise StopIteration


class Combine_Arcticle:
    def __init__(self, articles: List[Article]) -> None:
        self.articles = articles
        self.largest_len = 0

    def find_largest_articel(self):
        for article in self.articles:
            article_len = article.len()
            self.largest_len = (
                article_len if article_len > self.largest_len else self.largest_len
            )

    def match_articels(self):
        self.find_largest_articel()
        # print(self.largest_len)
        for article in self.articles:
            article.matching(self.largest_len)

    def combine(self):
        result = ""
        while True:
            text = ""
            try:
                for article in self.articles:
                    text += " ".join(next(article)) + " "
                text = text.strip()
                text += ".\n"
            except StopIteration:
                break
            result += text
        return result
