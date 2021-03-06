import requests
from bs4 import BeautifulSoup

"""
I've recently dealt with the issue of extremely long wait times while waiting for care from the emergency room
Two visits, days apart, over a 50% reduction in wait time based on location choosen
This spawned the idea of creating a application to aggregate wait data based on ones location within a specific radius
I'll be walking through the steps I take to get there with this being the first point

Objectives
    Retrieve data from website
    Parse data for wait times
"""

url = "https://www.upstate.edu/healthcare/wait.php"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
time = soup.find_all('div', {'class': 'emergency-times'})
print(time)
