import requests
"""
Objectives
    Send an HTTP request to a URL received from the user input.
    Print out the Quote content extracted from the json body response.
    Print out the Invalid
"""


print("Input the URL:")
input_url = input()

r = requests.get(input_url)
if r.status_code >= 200 and r.status_code < 400:
    try:
        print(r.json()['content'])
    except:
        print("Invalid quote resource")
else:
    print("Invalid quote resource")