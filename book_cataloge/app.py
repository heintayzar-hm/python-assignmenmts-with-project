import env_packages as env
import c_io
import book_package.book_module as Book

class App:
    def __init__(self):
        self.book = Book.BookModule()

    def run(self):
        user_choice = input(env.users_choice_text)

        if(user_choice == '6'):
            return print(env.good_bye_text)

        if user_choice == '1':
            self.add_book()
        elif user_choice == '2':
            self.view_books()
        else:
            print("Not implement Yet")

        self.run()

    def add_book(self):
        self.book.add_book()

    def view_books(self):
        self.book.view_books()

