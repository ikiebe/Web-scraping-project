import requests
from bs4 import BeautifulSoup

URL = "https://blog.grabcad.com/blog/2018/09/06/these-are-the-10-highest-paid-engineering-degrees/"

response = requests.get(URL)
tx = response.text

soup = BeautifulSoup(tx, 'html.parser')
eng = soup.find_all(name="strong")
h = eng[::-1]

for e in h:
    o = e.text
    print(o)

with open('engineering.txt', mode="w") as file:
    for each in h:
        file.write(f"{each.text}\n")

