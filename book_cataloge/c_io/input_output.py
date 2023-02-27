from urllib.parse import urlparse
from datetime import datetime
from .output_color import *
def check_url(url):
        parsed_url = urlparse(url)
        if parsed_url.scheme and parsed_url.netloc:
            return True
        return False

def error_msg(): # error massage
        print(red('Please enter a valid url'))


def get_url(prompt):
     string_url = input(prompt)
     if(check_url(string_url)):
         return string_url
     else:
         error_msg()
         return get_input(prompt, "url")

def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print(red('Please enter a valid number'))
        return get_input(prompt, "int")

def get_str(prompt):
    try:
        string = input(prompt)
        if(len(string.strip()) == 0 or len(string.strip()) > 50):
            print(red("Please enter a string that is between 1 and 50 characters long"))
            return get_input(prompt, "str")
        return string
    except ValueError:
        print(red('Please enter a valid string'))
        return get_input(prompt, "str")

def get_date(prompt):
    try:
        date = input(prompt)
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        return date
    except ValueError:
        print(red('Please enter a valid date'))
        return get_input(prompt, "date")

def get_input(prompt, valid_type):
    prompt = cyan(prompt)
    if(valid_type == "url"):
        return get_url(prompt)
    elif(valid_type == "int"):
        return get_int(prompt)
    elif(valid_type == "str"):
        return get_str(prompt)
    elif(valid_type == "date"):
        return get_date(prompt)
    else:
        raise Exception("Invalid type")

def print_book_list(books):
    if(len(books) == 0):
        print(red("No book to show!!"))
        return
    else:
        for i, book in enumerate(books):
            print(f"\n{cyan('Index: ')}{i+1}")
            print(f"{cyan('Book author: ')}{book['author']}")
            print(f"{cyan('Book name: ')}{book['name']}")
            print(f"{cyan('Book date: ')} {book['date']}")
            print(f"{cyan('Book url: ')} {book['url']}\n")

def successful_add_msg():
    print(green("\nBook added successfully\n"))

def successful_delete_msg():
    print(green("\nBook deleted successfully\n"))

def successful_edit_msg():
    print(green("\nBook edited successfully\n"))

def successful_exit_msg():
    print(green("\nBye Bye\n"))
