from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Define the fields we want to test
field_names = ['firstname', 'lastname', 'email']


# Define a function to test a single field
def test_field(driver, field_name):
    try:
        # Find the input field by its name attribute
        input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//input[@name='{field_name}']")))

        # Enter a test value into the input field
        input_field.clear()
        input_field.send_keys('Test Value')

        # Submit the form
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_button.click()

        # Verify that the value was entered correctly
        result = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value((By.XPATH, f"//input[@name='{field_name}']"), 'Test Value'))
        assert result, f'Failed to enter value into {field_name} field'

    except Exception as e:
        print(f'Test failed: {e}')


# Use a context manager to ensure the browser is always closed
with webdriver.Firefox() as driver:
    # Navigate to the web page
    driver.get('https://app.cloudqa.io/home/AutomationPracticeForm')

    # Loop through the fields and test each one
    for field_name in field_names:
        test_field(driver, field_name)
