import requests

from bs4 import BeautifulSoup

"""
Objectives
    Feed the program a link to a movie description. This is an example of a
correct link: https://www.imdb.com/title/tt0080684/.
    Inspect the page and find out how the movie's title and description are
stored in the source code.
    Download the webpage content, parse it using the beautifulsoup library,
and print out the movie's original title and description in a dictionary.
"""
'''
Previous Code for retrieving a quote
def get_quote(url):
    r = requests.get(url)
    if r.status_code >= 200 and r.status_code < 400:
        try:
            return r.json()['content']
        except:
            return "Invalid movie page!"
    else:
        return "Invalid movie page!"
'''
def get_title_description(url):
    movie = {}
    r = requests.get(url)
    if r.status_code >= 200 and r.status_code < 400:
        try:
            soup = BeautifulSoup(r.content, 'html.parser')
            movie['title'] = (soup.find('h1')).text
            movie['description'] = (soup.find('div', {'class': "summary_text"})).text
            return movie
        except:
            return ("Invalid movie page!")
    else:
        return ("Invalid movie page!")

print("Input the URL:")
input_url = input()
print(get_title_description(input_url))

