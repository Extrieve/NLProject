import requests
import re
from datetime import datetime as dt

r = requests.get('https://a.4cdn.org/pol/catalog.json')
r = r.json()
print(r[0]["threads"])

def gen_chan():
    for idx, page in enumerate(r):
        print(idx, page)
        for thread in r[idx]['threads']:
            yield thread
            break

def get_threads(key: str, default='NaN'):
    return threads.get(key, default)

parsed_posts = list()


# Refactored code
for threads in gen_chan():
    title = get_threads('com')
    re.sub(r'<.*?>', '', title)
    # Remove all html tags
    # only A-Z, a-z, 0-9, and spaces
    title = re.sub(r'<.*?>', '', title)
    title = re.sub(r'[^A-Za-z0-9 ]', '', title)
    print(title, '\n')
    if 'last_replies' in threads:
        for comment in threads['last_replies']:
            current = dict()
            current['title'] = title
            current['com'] = get_threads('com')
            current['com'] = comment.get('com', 'NaN')
            current['resto'] = comment.get('resto', 'NaN')
            current['now'] = comment.get('now', 'NaN')
            current['time'] = comment.get('time', 'NaN')
            current['filename'] = comment.get('filename', 'NaN')
            current['url'] = comment.get('com')

            parsed_posts.append(current)

for post in parsed_posts[1:]:
    print(post['title'])