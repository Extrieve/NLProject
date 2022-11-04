import requests
import json
import re, string


def clean_text(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def main():
    r = requests.get('https://a.4cdn.org/pol/catalog.json')
    r = r.json()
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

    filename = '4chan/Data/data_chan.json'
    # check if file exists, if yes add to it, if no create it
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            data.update(all_posts)

    except FileNotFoundError:
        data = all_posts

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    

    # with open('data_chan.json', 'w') as f:
    #     json.dump(all_posts, f, indent=4)


if __name__ == '__main__':
    main()