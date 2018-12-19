import requests
response = requests.get('http://yelp.com')

print(response.url)
print(response.text)
