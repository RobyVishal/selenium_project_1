from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to ChromeDriver (ensure you have placed chromedriver in your project folder)
service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Wait for the search box to be visible and clickable (up to 10 seconds)
search_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "q"))
)

# Using JavaScript to focus and interact with the search box
driver.execute_script("arguments[0].focus();", search_box)
driver.execute_script("arguments[0].setAttribute('value', 'Selenium WebDriver');", search_box)

# Simulate pressing Enter using JavaScript
search_box.send_keys(Keys.RETURN)

# Print the page title
print(driver.title)

# Close the browser
driver.quit()




