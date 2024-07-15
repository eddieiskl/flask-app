# test_requests.py
import requests

response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
print(response.status_code)