import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import (
   WebDriverException, NoSuchElementException)

SCRAPE_URL = ("http://international.o2.co.uk/internationaltariffs/"
   "calling_abroad_from_uk")

def get_calling_cost(country):
   """
   Get the per minute calling cost to a landline in a specific country 
   on an O2 monthly contract.

   Keyword arguments:
   country -- the country name to query

   Returns: string representing the cost
   """
   try:
      driver = webdriver.Chrome()
      driver.get(SCRAPE_URL)
   
      # Search on country in search form
      search_element = driver.find_element_by_id("countryName")
      search_element.click()
      search_element.send_keys(country)
      search_element.send_keys(Keys.ENTER)
   
      # Wait for element to be present, then open the pay monthly tab
      try:
         driver.implicitly_wait(5)
         tab_element = driver.find_element_by_id("paymonthly")
         tab_element.click()
      except NoSuchElementException:
         raise ValueError("Country not found or scrape page changed")
   
      # On the correct page, use xpath to find the calling cost - found in
      # a specific table on the following table cell after content 'Landline'
      cost_element = driver.find_element_by_xpath(
         "//table[@id='standardRatesTable']"
         "//td[.='Landline']/following-sibling::td")
      return cost_element.text

   except WebDriverException:
      raise RuntimeError("Error using Chrome WebDriver or scrape page changed")

   finally:
      # Using driver.close() raises subprocess exceptions in Windows
      driver.quit()

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description=
      "Get the per minute calling cost to a landline in a specific country "
      "on an O2 monthly contract through web scraping. Finds costs for a "
      "set list of countries by default, otherwise specify a country.")
   parser.add_argument("--country", help="Name of country to query")
   args = parser.parse_args()

   DEFAULT_COUNTRIES = ['Canada', 'Germany', 'Iceland', 'Pakistan',
      'Singapore', 'South Africa']
   try:
      if(args.country):
         print(args.country, ": ", get_calling_cost(args.country))
      else:
         for country in DEFAULT_COUNTRIES:
            print(country, ": ", get_calling_cost(country))
   except (ValueError, RuntimeError) as e:
      print(e.args)
