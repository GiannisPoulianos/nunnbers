import requests

url = "https://www.basketball-reference.com/friv/numbers.fcgi?number=00&year="
response = requests.get(url)

print(response.text)