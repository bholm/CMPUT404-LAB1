import requests

r = requests.get('https://raw.githubusercontent.com/bholm/CMPUT404-LAB1/master/lab1.py')

print(r.content.decode("utf-8"))
