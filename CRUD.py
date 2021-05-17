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
        self.data = []
        self.id = 0

    def addPost(self, author, post):
        post = Post(self.id, author, post)
        self.id += 1

        self.data.append(post)
        return post

    def getPost(self, id):
        for post in self.data:
            if post.id == id:
                return post

        raise POSTNOTFOUND

    def getAllPosts(self):
        return self.data

    def delete(self, id):
        for post in self.data:
            if post.id == id:
                self.data.remove(post)
                return

    def save(self):
        fieldnames = ["id", "author", "post"]
        with open("records.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for post in self.data:
                writer.writerow(asdict(post))
            
    def load(self):
        self.data = []

        with open("records.csv", "r", newline="") as f:
            reader = csv.DictReader(f)
            for data in reader:
                post = self.addPost(data["author"], data["post"])
                post.id = int(data["id"])
