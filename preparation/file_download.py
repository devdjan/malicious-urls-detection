import requests

print('Downloading file using requests')

url = 'https://ransomwaretracker.abuse.ch/downloads/RW_URLBL.txt'
r = requests.get(url)

with open('/Users/kirillkarpenok/files/practise/malicious-urls-detection/data/urls.csv', 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)

