import random
from book import Book

def generate_books(n):
    titles=["Book "+str(i) for i in range(n)]
    authors=["Author "+str(i%100) for i in range(n)]
    genres=["Sci-Fi","Romance","Horror","Mystery","Fantasy"]
    years=[random.randint(1900,2025) for _ in range(n)]
    ratings=[round(random.uniform(1.0,5.0),1) for _ in range(n)]
    books=[]
    for i in range(n):
        b=Book(titles[i],authors[i],random.choice(genres),years[i],ratings[i])
        books.append(b)
    return books
