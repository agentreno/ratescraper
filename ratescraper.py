from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

SCRAPE_URL = ("http://international.o2.co.uk/internationaltariffs/"
   "calling_abroad_from_uk")

def get_calling_cost(country):
   """
   Get the per minute calling cost to a landline in a specific country 
   on an O2 monthly contract.

   Keyword arguments:
   country -- the country name to query

   Returns: string
   """
   driver = webdriver.Chrome()
   driver.get(SCRAPE_URL)

   # Search on country in search form
   search_element = driver.find_element_by_id("countryName")
   search_element.click()
   search_element.send_keys(country)
   search_element.send_keys(Keys.ENTER)

   # Wait for element to be present, then open the pay monthly tab
   driver.implicitly_wait(10)
   tab_element = driver.find_element_by_id("paymonthly")
   tab_element.click()

   # Confirm standard rates presence
   return driver.find_element_by_id("standardRates")

if __name__ == "__main__":
   print(get_calling_cost("new zealand"))
