from flask import Blueprint, request
from dataclasses import dataclass


pb = Blueprint("biblioteca", __name__)

books = []

@dataclass
class Book:
    id: int
    name: str
    author: str
    
    def to_json(self):
        r = {
            "id": self.id,
            "name": self.name,
            "author": self.author,
        }
        return r


@pb.get("/livros")
def list_books():
    list_of_books = []
    for book in books:
        json = book.to_json()
        list_of_books.append(json)

    return list_of_books


@pb.post("/livros")
def create_books():
    json = request.json
    id = json["id"]
    name = json["name"]
    author = json["author"]
    
    book = Book(id, name, author)
    books.append(book)
    return {"id": book.id}
