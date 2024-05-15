from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.google.com")
driver.execute_script("window.open()")
driver.last_tab()
