from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Firefox used
driver = webdriver.Chrome()
# base url
driver.get("http://github.com/login")

username = driver.find_element(By.ID, "login_field")
password = driver.find_element(By.ID, "password")

# password and username need to go into these values
username.send_keys("enter email")
time.sleep(1)
password.send_keys("enter password")
time.sleep(1)

login_form = driver.find_element(By.XPATH, "//input[@value='Sign in']")
time.sleep(1)
login_form.click()
time.sleep(20)

# These are some of the most popular users on github
prepend = ["jashkenas", "ruanyf", "substack", "kennethreitz", "jlord", "daimajia", "mdo", "schacon", "mattt",
           "sindresorhus", "defunkt", "douglascrockford", "mbostock", "jeresig",
           "mojombo", "addyosmani", "paulirish", "vczh", "romannurik", "tenderlove", "chriscoyier", "johnpapa",
           "josevalim",
           "charliesome", "CoderMJLee", "ry", "antirez", "muan", "isaacs", "angusshire",
           "hadley", "hakimel", "yyx990803", "fat", "fabpot", "ibireme", "tekkub",
           "BYVoid", "laruence", "onevcat", "tpope", "mrdoob", "LeaVerou", "chrisbanes", "wycats", "lifesinger",
           "cloudwu", "mitsuhiko", "michaelliao", "ryanb", "clowwindy", "JacksonTian", "yinwang0", "Trinea",
           "pjhyett", "dhh", "gaearon"]

for user in prepend:
    for t in range(1, 100):
        string = "https://github.com/{}/?page={}&tab=followers".format(user, t)
        print("Following user {} in page {}".format(user, t))
        
        driver.get(string)
        time.sleep(5)

        follow_button = driver.find_elements(By.XPATH, "//input[@type='submit'][@value='Follow']")

        print("Follow butrto", follow_button)
        # Once page is loaded this clicks all buttons for follow
        try:
            for i in follow_button:
                i.submit()
                time.sleep(2)
        except:
            pass

driver.close()