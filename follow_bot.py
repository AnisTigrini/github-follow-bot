from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

driver.get("http://github.com/login")
username = driver.find_element(By.ID, "login_field")
password = driver.find_element(By.ID, "password")

username.send_keys("TBD")
time.sleep(1)
password.send_keys("TBD")
time.sleep(1)

login_form = driver.find_element(By.XPATH, "//input[@value='Sign in']")
time.sleep(1)
login_form.click()
time.sleep(5)

number = driver.find_element(By.XPATH, "//h3[@data-target='sudo-credential-options.githubMobileChallengeValue']")
print(number.get_attribute("innerHTML"))

time.sleep(15)

prepend = ["jashkenas", "ruanyf", "substack", "kennethreitz", "jlord", "daimajia", "mdo", "schacon", "mattt",
           "sindresorhus", "defunkt", "douglascrockford", "mbostock", "jeresig",
           "mojombo", "addyosmani", "paulirish", "vczh", "romannurik", "tenderlove", "chriscoyier", "johnpapa",
           "josevalim",
           "charliesome", "CoderMJLee", "ry", "antirez", "muan", "isaacs", "angusshire",
           "hadley", "hakimel", "yyx990803", "fat", "fabpot", "ibireme", "tekkub",
           "BYVoid", "laruence", "onevcat", "tpope", "mrdoob", "LeaVerou", "chrisbanes", "wycats", "lifesinger",
           "cloudwu", "mitsuhiko", "michaelliao", "ryanb", "clowwindy", "JacksonTian", "yinwang0", "Trinea",
           "pjhyett", "dhh", "gaearon"]

with open('data.json', 'r') as file:
    data = json.load(file)

currentUser = data["user"]
currentPage = data["page"]
maxPage = currentPage + 5

try:
    for user in prepend:
        if (currentUser == data['user']):
            while (currentPage < maxPage):
                string = "https://github.com/{}/?page={}&tab=followers".format(user, currentPage)
                print (string)
                driver.get(string)
                time.sleep(15)

                follow_button = driver.find_elements(By.XPATH, "//input[@type='submit'][@value='Follow']")

                for i in follow_button:
                    i.submit()
                    time.sleep(2)
                
                currentPage += 1

    driver.close()
    raise Exception("End of script")
except:
    data["page"] = currentPage

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)  # Use indent for pretty formatting
