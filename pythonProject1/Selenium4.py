import requests

# Send a POST request to the /cars endpoint
response = requests.post('http://localhost:5000/cars')
expected = "creating new car"
actual = response.text
assert expected == actual
expected = 201
actual = response.status_code
assert expected == actual

# Print the response text
print(response.text)