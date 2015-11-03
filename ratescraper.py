from selenium import webdriver

if __name__ == "__main__":
   driver = webdriver.Chrome()
   driver.get("http://www.cheese.com")
   print(driver.title)
