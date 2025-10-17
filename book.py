# book.py
# this file stores the Book class which holds all information about one book

class Book:
    def __init__(self, title, author, genre, year, rating):
        # store basic info for each book
        self.title=title
        self.author=author
        self.genre=genre
        self.year=year
        self.rating=rating

    def __str__(self):
        # this helps to print the book nicely
        return f"{self.title} by {self.author} ({self.year}) - {self.genre}, Rating: {self.rating}"
