import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import names

# API Testing

# 1. Testing Github API
repos = requests.get("https://api.github.com/users/avielb/repos")
assert len(repos.json()) >= 5, "Less than 5 repositories found."

# 2. Testing Agify API
for _ in range(3):
    name = names.get_first_name()
    age_response = requests.get(f"https://api.agify.io/?name={name}").json()
    assert 0 <= age_response["age"] <= 120, f"Age for name {name} is out of range: {age_response['age']}."

# 3. Testing Universities API
unis = requests.get("http://universities.hipolabs.com/search?country=Israel")
assert len(unis.json()) >= 5, "Less than 5 universities found in Israel."

# UI Testing

# Initialize Selenium WebDriver
driver_yc = webdriver.Chrome()
driver_docker = webdriver.Chrome()

# 4. Testing Y Combinator Title
driver_yc.get("https://www.ycombinator.com/")
assert driver_yc.title == "Y Combinator", "Y Combinator title is incorrect."

# 5. Testing Docker Hub Title with wait
driver_docker.get("https://hub.docker.com")
try:
    WebDriverWait(driver_docker, 10).until(EC.title_contains("Docker Hub"))
    assert driver_docker.title == "Docker Hub Container Image Library | App Containerization", "Docker Hub title is incorrect."
finally:
    # Close the drivers
    driver_yc.quit()
    driver_docker.quit()