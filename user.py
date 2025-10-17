# user.py
# stores user info such as name, borrowed books, and history

class User:
    def __init__(self, name):
        self.name=name
        self.borrowed_books=[]
        self.history=[]

    def borrow_book(self, book):
        # add book to borrowed list and history
        self.borrowed_books.append(book)
        self.history.append(book)
        print("📚 Book borrowed successfully:", book.title)

    def return_book(self, book):
        # remove book from borrowed list if it exists
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print("✅ Book returned successfully:", book.title)
        else:
            print("⚠️ You cannot return a book you didn’t borrow.")

    def show_history(self):
        # show all borrowed books
        print("\n📖 Borrowing History for", self.name)
        if not self.history:
            print("No history found.")
        else:
            for b in self.history:
                print(b)
