from urllib.parse import urlparse
from datetime import datetime

def check_url(url):
        parsed_url = urlparse(url)
        if parsed_url.scheme and parsed_url.netloc:
            return True
        return False

def error_msg(): # error massage
        print('\033[91m\nPlease enter a valid url\033[0m \n')


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
        print('\033[91m\nPlease enter a valid number\033[0m \n')
        return get_input(prompt, "int")

def get_str(prompt):
    try:
        string = input(prompt)
        if(len(string.strip()) == 0 or len(string.strip()) > 50):
            print("Please enter a string that is between 1 and 50 characters long")
            return get_input(prompt, "str")
        return string
    except ValueError:
        print('\033[91m\nPlease enter a valid string\033[0m \n')
        return get_input(prompt, "str")

def get_date(prompt):
    try:
        date = input(prompt)
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        return date
    except ValueError:
        print('\033[91m\nPlease enter a valid date\033[0m \n')
        return get_input(prompt, "date")

def get_input(prompt, valid_type):
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
