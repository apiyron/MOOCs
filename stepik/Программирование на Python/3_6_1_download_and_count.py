import requests

with open('dataset_3378_2.txt', 'r') as f:
    url = f.readline().strip()
    print(url)
    r = requests.get(url, allow_redirects=True)
    open('3_6_1_file.txt', 'wb').write(r.content)
with open('3_6_1_file.txt', 'r') as f:
    lines = f.read().splitlines()
print(len(lines))