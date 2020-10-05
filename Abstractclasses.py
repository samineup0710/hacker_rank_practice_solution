""" problem statement link : https://www.hackerrank.com/challenges/30-abstract-classes/problem """
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
class MyBook(Book):
    def __init__(self, title, aurthor, price):
        self.title=title
        self.author=author
        self.price = price
    def display(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Price: {}".format(self.price))
    
#Write MyBook class

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()