import requests
"""
Objectives
    Send an HTTP request to a URL received from the user input.
    Print out the Quote content extracted from the json body response.
    Print out the Invalid
"""

def get_quote(url):
    r = requests.get(url)
    if r.status_code >= 200 and r.status_code < 400:
        try:
            return r.json()['content']
        except:
            return "Invalid quote resource"
    else:
        return "Invalid quote resource"

print("Input the URL:")
input_url = input()
print(get_quote(input_url))