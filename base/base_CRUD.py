# backend
import csv
from dataclasses import dataclass, asdict


@dataclass
class Post:
    id: int
    author: str
    post: str

class POSTNOTFOUND(Exception):
    pass

class App:
    def __init__(self):
        pass

    def addPost(self, author, post):
        pass

    def getAllPosts(self):
        pass

    def getPost(self, id):
        pass

    def delete(self, id):
        pass

    def save(self):
        pass

    def load(self):
        pass