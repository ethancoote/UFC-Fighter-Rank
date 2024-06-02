# Gets winner, loser, weight class, and date of every UFC fight
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def init_dataset():

    url = "http://www.ufcstats.com/statistics/events/completed?page=all"
    driver = getDriver()
    driver.get(url)
    element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, "b-statistics__table-row")))
    html = driver.find_elements('class name', "b-statistics__table-row")
    for item in html:
        print(item.text)
        
def getDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    userAgent = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    userAgent += "Chrome/121.0.0.0 Safari/537.36"
    options.add_argument(userAgent)
    try:
        driver = webdriver.Chrome(options=options)
    except Exception as e:
        print(f"Error: Failed to initialize driver [ {e} ]")

    return driver
    