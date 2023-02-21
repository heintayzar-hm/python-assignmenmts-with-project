import app
import env

def get_input(prompt): # get input from user
    return error_handler(prompt)

def main():
    application = app.App()
    application.run()
main()

