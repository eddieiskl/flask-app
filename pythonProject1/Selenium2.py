from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the Tip Calculator web page
driver.get("file:///Users/MacBook/Downloads/tip_calc/index.html")

# Wait for 5 seconds to ensure the page is fully loaded
sleep(5)

# Find the elements on the page
bill_amount_input = driver.find_element(By.ID, "billamt")
service_quality_select = Select(driver.find_element(By.ID, "serviceQual"))
music_satisfaction_select = Select(driver.find_element(By.ID, "musicSatisfaction"))
people_amount_input = driver.find_element(By.ID, "peopleamt")
calculate_button = driver.find_element(By.ID, "calculate")
tip_amount_display = driver.find_element(By.ID, "tip")

# Possible values for each input field
bill_amounts = [50, 100, 150, 200, 250, 300]
service_qualities = ["30% - Outstanding", "20% - Good", "15% - It was OK", "10% - Bad", "5% - Terrible"]
music_satisfactions = [1, 2, 3, 4, 5]
number_of_people = [1, 2, 3, 4, 5]

# Open a log file to save the test results
log_file = open("test_results.txt", "w")


# Function to perform a test
def test_tip_calculator(bill, service_quality, music_satisfaction, people, expected_tip):
    # Input values into the fields
    bill_amount_input.clear()
    bill_amount_input.send_keys(str(bill))

    service_quality_select.select_by_visible_text(service_quality)
    music_satisfaction_select.select_by_value(str(music_satisfaction))

    people_amount_input.clear()
    people_amount_input.send_keys(str(people))

    # Click the calculate button
    calculate_button.click()

    # Allow some time for the calculation and update
    sleep(1)  # Adjust sleep time as necessary

    # Verify the displayed tip amount
    tip_amount = tip_amount_display.text
    if tip_amount == f"${expected_tip:.2f}":
        result = f"Test passed: Bill {bill}, Service Quality {service_quality}, Music Satisfaction {music_satisfaction}, People {people}. Expected ${expected_tip:.2f}, got {tip_amount}\n"
        print(result)
        log_file.write(result)
    else:
        result = f"Test failed: Bill {bill}, Service Quality {service_quality}, Music Satisfaction {music_satisfaction}, People {people}. Expected ${expected_tip:.2f}, but got {tip_amount}\n"
        print(result)
        log_file.write(result)


# Run tests for all combinations
for bill in bill_amounts:
    for service_quality in service_qualities:
        for music_satisfaction in music_satisfactions:
            for people in number_of_people:
                # Calculate the expected tip amount
                service_percent = float(service_quality.split('%')[0]) / 100
                expected_tip = (bill * service_percent) / people + (music_satisfaction * people)
                # Run the test case
                test_tip_calculator(bill, service_quality, music_satisfaction, people, expected_tip)

# Close the WebDriver
driver.quit()

# Close the log file
log_file.close()