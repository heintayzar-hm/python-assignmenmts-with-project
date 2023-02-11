from urllib.parse import urlparse
import app

def check_url(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme and parsed_url.netloc:
        return True
    return False

def error_msg(): # error massage
   print('\033[91m\nPlease enter a valid url\033[0m \n')


def error_handler(prompt): # error handler for non integer input
     string_url = input(prompt)
     if(check_url(string_url)):
         return string_url
     else:
         error_msg()
         error_handler(prompt)
  
  

def get_input(prompt): # get input from user
    return error_handler(prompt)

def main():
    url = get_input(prompt = "Enter a url: ")
    app.run(url)
    app_continue = input("\n Do you want to continue? (y/n): ")
    if(app_continue.lower() == 'y'):
        main()
    else:
        print("\n Thank you for using this app")
    
main()

