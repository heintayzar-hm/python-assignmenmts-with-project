from c_io import get_input
from env_packages import env
class BookModule:
       def __init__(self):
           self.books = []

       def add_book(self):
           self.books.append({
            "name": get_input(env.add_book_dict["get_name"], "str"),
            "author": get_input(env.add_book_dict["get_author"], "str"),
            "date": get_input(env.add_book_dict["get_date"], "date"),
            "url": get_input(env.add_book_dict["get_url"], "url")
            })
           print("Book added successfully")

       def view_books(self):
           for i, book in enumerate(self.books):
               print(f"Index: {i+1}")
               print(f"Book name: {book['name']}")
               print(f"Book author: {book['author']}")
               print(f"Book date: {book['date']}")
               print(f"Book url: {book['url']}\n")
