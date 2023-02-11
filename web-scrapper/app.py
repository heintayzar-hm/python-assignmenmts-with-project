import requests
import os
import datetime
from bs4 import BeautifulSoup

def run(url = 'https://www.google.com'):
    html_obj = scrapper(url)
    folder_name = "scraping_results"
    try:
        folder_creator(folder_name)
        file_creator(folder_name, html_obj.title.text , html_obj.prettify())
        print("Scraping completed successfully")
    except Exception as e:
        print(e)

def scrapper(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        return soup
    else:
        print("Failed to get data from the website")
        
def folder_creator(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

def file_creator(folder_name, title, html_content):
    file_name = f"{title}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html"
    file_path = os.path.join(folder_name,file_name)
    write_to_file(file_path, html_content)
    return file_name

def write_to_file(file_path,html_content):
    with open(file_path, "w") as file:
        file.write(html_content)
