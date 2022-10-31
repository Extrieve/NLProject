from bs4 import BeautifulSoup
import pandas as pd
import re
import requests


def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    return text

url = 'https://en.wikipedia.org/wiki/List_of_ethnic_slurs'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
tables = soup.find_all('table', {'class': 'wikitable'})


# table rows have 4 columns: Term, Location, Target and Meaning
data_complete = list()

for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        data = row.find_all('td')
        if len(data) == 5:
            cur = list()
            for value in data:
                cur.append(clean_text(value.text))
            data_complete.append(cur)

df = pd.DataFrame(data_complete, columns=['Term', 'Location', 'Target', 'Meaning', 'Source'])

# Drop last column
df = df.drop(df.columns[-1], axis=1)
df.to_csv('ethnic_slurs.csv', index=False)

# for row in table.find_all('tr')[1:]:
#     cells = row.find_all('td')

#     term = cells[0].text
#     location = cells[1].text
#     target = cells[2].text
#     meaning = cells[3].text
    
