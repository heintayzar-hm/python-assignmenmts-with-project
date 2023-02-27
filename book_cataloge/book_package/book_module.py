from c_io import *
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
           successful_add_msg()

       def view_books(self):
           print_book_list(books=self.books)

       def search_book(self):
           search_term = get_input(env.search_book_dict["get_search_term"], "str")
           search_result = self.search(search_term)
           print_book_list(books=search_result)

       def delete_book(self):
           delete_book_index = get_input(env.delete_book_dict["get_delete_book_index"], "int")
           self.books = self.books[:delete_book_index - 1] + self.books[delete_book_index:]
           successful_delete_msg()

       def edit_book(self):
            edit_book_index = get_input(env.edit_book_dict["get_edit_book_index"], "int")
            print_book_list(books=[self.books[edit_book_index - 1]])
            new_book = {
            "name": get_input(env.add_book_dict["get_name"], "str"),
            "author": get_input(env.add_book_dict["get_author"], "str"),
            "date": get_input(env.add_book_dict["get_date"], "date"),
            "url": get_input(env.add_book_dict["get_url"], "url")
            }
            self.books = self.books[:edit_book_index - 1] + [new_book] + self.books[edit_book_index:]
            successful_edit_msg()
       def search(self,search_term):
            return [book for book in self.books if search_term.lower() in book['name'].lower()]
