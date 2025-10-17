# library.py
# manages a collection of books and provides search and recommendation features

from book import Book
import time

class Library:
    def __init__(self):
        self.books=[]
        self.book_index={}  # for fast lookup by title

    def add_book(self, book):
        # add a new book to library
        self.books.append(book)
        self.book_index[book.title.lower()]=book

    def remove_book(self, title):
        # remove book by title
        self.books=[b for b in self.books if b.title!=title]
        if title.lower() in self.book_index:
            del self.book_index[title.lower()]

    def show_all_books(self):
        # show all books
        print("\n📚 All Books in Library:")
        for b in self.books:
            print(b)

    # basic search (linear)
    def search_books(self, keyword, author=None, genre=None):
        results=[]
        for b in self.books:
            if (keyword.lower() in b.title.lower() or
                keyword.lower() in b.author.lower() or
                keyword.lower() in b.genre.lower()):
                if (author is None or author.lower()==b.author.lower()) and \
                   (genre is None or genre.lower()==b.genre.lower()):
                    results.append(b)
        print(f"🔎 Found {len(results)} book(s) matching your search.\n")
        return results

    # basic recommendation (top rated)
    def top_rated(self, n=3):
        sorted_books=sorted(self.books, key=lambda b:b.rating, reverse=True)
        return sorted_books[:n]

    # improved search (dictionary)
    def fast_search(self, title):
        key=title.lower()
        if key in self.book_index:
            return [self.book_index[key]]
        else:
            return []

    # improved recommendation (same genre, high rating)
    def similar_genre(self, genre, min_rating=4.5):
        results=[]
        for b in self.books:
            if b.genre.lower()==genre.lower() and b.rating>=min_rating:
                results.append(b)
        return results

    # compare base vs improved search time
    def compare_search_speed(self, test_titles):
        print("⏱️ Comparing search times...\n")
        start=time.time()
        for t in test_titles:
            self.search_books(t)
        base_time=time.time()-start

        start=time.time()
        for t in test_titles:
            self.fast_search(t)
        fast_time=time.time()-start

        print(f"{'Books Searched':<20}{'Base Search (s)':<20}{'Fast Search (s)'}")
        print("-"*60)
        print(f"{len(test_titles):<20}{base_time:<20.6f}{fast_time:.6f}")
