from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

link = 'https://www.python.org/'
driver.get(link)

locator = "//h2[text()='Upcoming Events']/../ul/li"
events_list = driver.find_elements(By.XPATH, locator)


def get_event_data(event):
    event_date = event.find_element(By.CSS_SELECTOR, "time").text
    event_name = event.find_element(By.CSS_SELECTOR, "a").text
    print(f"{event_date} {event_name}")
    return {f"{event_date}": f"{event_name}"}


result = {events_list.index(n): get_event_data(n) for n in events_list}
print(result)
time.sleep(500)
