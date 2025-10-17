# test_cases.py
# main file that tests all library functions and prints a final report

from book import Book
from library import Library
from user import User
from data_generator import generate_books

# --- create library and sample data ---
lib=Library()
lib.add_book(Book("Atomic Habits","James Clear","Self-Help",2018,4.8))
lib.add_book(Book("Dune","Frank Herbert","Sci-Fi",1965,4.6))
lib.add_book(Book("1984","George Orwell","Dystopian",1949,4.9))
lib.add_book(Book("The Martian","Andy Weir","Sci-Fi",2011,4.7))
lib.add_book(Book("The Hobbit","J.R.R. Tolkien","Fantasy",1937,4.8))

# --- create a user ---
u1=User("Mohamed")
u1.borrow_book(lib.books[0])
u1.return_book(lib.books[0])

# --- show all books ---
lib.show_all_books()

# --- base search test ---
print("\n🔍 Search for 'sci':")
for b in lib.search_books("sci"):
    print(b)

# --- base recommendation test ---
print("\n🏆 Top 3 Rated Books:")
for b in lib.top_rated(3):
    print(b)

# --- improved search test ---
print("\n⚡ Fast Search for '1984':")
for b in lib.fast_search("1984"):
    print(b)

# --- improved recommendation test ---
print("\n🎯 Similar Genre (Sci-Fi) with Rating ≥ 4.5:")
for b in lib.similar_genre("Sci-Fi"):
    print(b)

# --- timing test (smaller dataset for class presentation) ---
print("\n📊 Timing Comparison Test:")
fake_books=generate_books(2000)
for b in fake_books:
    lib.add_book(b)
lib.compare_search_speed(["Book 10","Book 500","Book 1500"])

# --- FINAL REPORT SECTION ---
print("\n==================== 📘 SMART LIBRARY REPORT ====================")
print("Total Books in System:", len(lib.books))
print("Total Unique Titles Indexed:", len(lib.book_index))
print("Most Popular Genre Example: Sci-Fi")
print("Example User:", u1.name)
print("Books Borrowed:", len(u1.history))
print("Top Rated Books:")
for b in lib.top_rated(3):
    print(" -", b.title, "(Rating:", b.rating, ")")
print("===============================================================")
