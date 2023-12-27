import time

from selenium import webdriver


# Create a new instance of the Chrome drivers
chrome_path="/usr/local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_path)
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')

try:
    # Open the web app in the browser
    driver.get("http://127.0.0.1:5000/users/get_user_id/5")

    # Wait for the page to load
    driver.implicitly_wait(60)
    time.sleep(20)



finally:
    # Close the browser window
    driver.quit()
