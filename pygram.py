'''
Python Instagram Bot to automate:
 - likes
 - follows
 - unfollows
'''

from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()       # Creates a Firefox browser object / session.
browser.implicitly_wait(5)          # sets selenium waiting time for 5 seconds (i.e., 5 seconds before retry)

browser.get("https://www.instagram.com/")   # gets the URL page

login_link = browser.find_element_by_xpath("//a[text()='Log in']")      # uses XPath (the native language for
                                                                        # locading nodes in XML) to find the
                                                                        # Login prompt.
login_link.click()  # "clicks" on the aforementioned link

sleep(5)    # waits for 5 seconds.

browser.close()

