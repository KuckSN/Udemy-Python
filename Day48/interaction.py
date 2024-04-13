from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

first_name.send_keys("")
last_name.send_keys("")
email.send_keys("")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()
# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

# event_times = driver.find_elements(By.CSS_SELECTOR, value=".event_widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# events = {}

# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }


# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# prince_cents =driver.find_element(By.CLASS_NAME, value = "a-price-fraction")

# print(f"The price is {price_dollar.text}.{prince_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# button = driver.find_element(By.ID, value="submit")
# print(button.size)


# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# docs_link = driver.find_element(By.XPATH, value='/html/body/div[1]/footer/div/nav/ul/li[5]/a')
# print(docs_link.text)

# driver.find_elements(By.NAME)

# driver.close()
driver.quit()