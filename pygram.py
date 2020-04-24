'''
Python Instagram Bot to automate:
 - likes
 - follows
 - unfollows

Consider running from terminal including arguments for login credentials.

Example:

    % python pygram(username, password)

'''

from time import sleep
from selenium import webdriver

browser = webdriver.Safari()        # Creates a Safari browser object / session.
browser.implicitly_wait(5)          # sets selenium waiting time for 5 seconds (i.e., 5 seconds before retry)

browser.get("https://www.instagram.com/")   # gets the URL page

###
### Originally used browser.find_element_by_xpath(str) method to click on the login box,
### but Safari seems too default to this field.
###
### Similarly, there's no need to object.click either.
###

#login_link = browser.find_element_by_xpath("//a[text()='Log in']")
#login_link.click()  # "clicks" on the aforementioned link

sleep(2)            # waits for 2 seconds.

username_input = browser.find_element_by_css_selector("input[name='username']")     # This is where the field is found
password_input = browser.find_element_by_css_selector("input[name='password']")     # This is where the field is found

username_input.send_keys("<your username>")     # This is where your username information goes.
password_input.send_keys("<your password>")     # This is where your password goes.

# browser.close()

