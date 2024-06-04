# Gets winner, loser, weight class, and date of every UFC fight
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

all_fight_results = []

def init_dataset():

    all_links = []
    url = "http://www.ufcstats.com/statistics/events/completed?page=all"
    driver = get_driver()
    driver.get(url)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, "a")))
    html = driver.find_elements('css selector', "a")

    for item in html:
        if 'http://www.ufcstats.com/event-details/' in str(item.get_attribute('href')):
            all_links.append(item.get_attribute('href'))
    driver.close()

    del all_links[0]
    for link in all_links:
        get_event_results(link)

    # this is the first UFC event. It is not listed on the events list page, so I've added it manually
    get_event_results("http://www.ufcstats.com/event-details/6420efac0578988b")
    return all_fight_results

def get_event_results(event_link):
    outcomes = []
    weight_classes = []

    driver = get_driver()
    driver.get(event_link)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, "b-flag__text")))
    win_flags = driver.find_elements('class name', "b-flag__text")
    fighter_names = driver.find_elements('css selector', "a.b-link.b-link_style_black")
    table_text = driver.find_elements('css selector', "p.b-fight-details__table-text")

    for flag in win_flags:
        # one outcome is added for each fighter
        outcomes.append(flag.text)
        if (flag.text == "WIN"):
            outcomes.append("LOSS")
        elif (flag.text != "DRAW" and flag.text != "NC"):
            outcomes.append(flag.text)
             
    for item in table_text:
        if "weight" in str(item.text).lower():
            # added twice to match outcomes indexes
            weight_classes.append(item.text)
            weight_classes.append(item.text)

    i = 0 # this will iterate through the outcomes list, to see if the fight was a win, a draw, or other
    fight_outcome = []
    for fighter in fighter_names:
        fight_outcome.append(fighter.text)
        fight_outcome.append(outcomes[i])
        if not i%2 == 0:
            all_fight_results.append([fight_outcome[0], fight_outcome[1], fight_outcome[2], fight_outcome[3], weight_classes[i]])
            fight_outcome.clear()
        i+=1

    driver.close()
    return all_fight_results


def get_driver():
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
    