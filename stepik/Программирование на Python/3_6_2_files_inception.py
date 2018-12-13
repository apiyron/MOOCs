import requests

base_url = 'https://stepic.org/media/attachments/course67/3.6.3/'
count = 0
with open('dataset_3378_3.txt', 'r') as f:
    url = f.readline().strip()
    print(url)
    r = requests.get(url, allow_redirects=True)
    while True:
        print(r.text)
        if r.text[0:2] == 'We':
            res = base_url+url
            break
        else:
            url = r.text
            r = requests.get(base_url+url, allow_redirects=True)
        count += 1
print("Files:", count)
print(res)