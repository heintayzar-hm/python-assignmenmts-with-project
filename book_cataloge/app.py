import env
from input_module import get_input
class App:
    def __init__(self):
        self.books = []

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
        self.books.append({
            "name": get_input(env.add_book_dict["get_name"], "str"),
            "author": get_input(env.add_book_dict["get_author"], "str"),
            "date": get_input(env.add_book_dict["get_date"], "date"),
            "get_url": get_input(env.add_book_dict["get_url"], "url")
        })
        print("Book added successfully")

    def view_books(self):
            for i, book in enumerate(self.books):
                print(f"Index: {i+1}")
                print(f"Book name: {book['name']}")
                print(f"Book author: {book['author']}")
                print(f"Book date: {book['date']}")
                print(f"Book url: {book['get_url']}\n")


