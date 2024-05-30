# Gets winner, loser, weight class, and date of every UFC fight
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def init_dataset():

    url = "http://www.ufcstats.com/statistics/events/completed?page=all"
    driver = getDriver()
    driver.get(url)
    time.sleep(1) # wait for root to be fully loaded
    mainPage = BeautifulSoup(driver.page_source, 'html.parser')
    print(mainPage.prettify())
        
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
    