from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_disability-related_terms_with_negative_connotations'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')

# find every ul element
list = soup.find_all('ul')
data = []
for li in list:
    # find all the li elements
    print(li.text)
    if '[' in li.text and ']' in li.text:
        data.append(li.text)

df = pd.DataFrame(data, columns=['Term'])
df.to_csv('disabilities_data.csv', index=False)
