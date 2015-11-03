from selenium import webdriver

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
   return driver.title

if __name__ == "__main__":
   print(get_calling_cost("new zealand"))
