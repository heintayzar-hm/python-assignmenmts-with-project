import env_packages as env
from c_io import *
import book_package.book_module as Book

class App:
    def __init__(self):
        self.book = Book.BookModule()

    def run(self):
        user_choice = input(env.users_choice_text)

        if(user_choice == '6'):
            return successful_exit_msg()

        if user_choice == '1':
            self.book.add_book()
        elif user_choice == '2':
            self.book.view_books()
        elif user_choice == '3':
            self.book.search_book()
        elif user_choice == '4':
            self.book.delete_book()
        elif user_choice == '5':
            self.book.edit_book()
        else:
            print(red("\nInvalid Input\n"))

        self.run()


