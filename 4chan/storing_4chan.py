import requests
import json
import re, string

r = requests.get('https://a.4cdn.org/g/catalog.json')
r = r.json()

def clean_text(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

all_posts = dict()
for page in r:
    for thread in page['threads']:
        
        if 'com' not in thread:
            continue

        title = thread['com']
        title = clean_text(title)
        all_posts[title] = list()


        if 'last_replies' not in thread:
            continue

        for post in thread['last_replies']:
            if 'com' not in post:
                continue

            parsed_post = post['com']
            parsed_post = clean_text(parsed_post)
            all_posts[title].append(parsed_post)
            print(parsed_post)


print(len(all_posts))

with open('data_chan_games.json', 'w') as f:
    json.dump(all_posts, f, indent=4)