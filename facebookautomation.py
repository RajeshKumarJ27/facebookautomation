# Use mozilla firefox browser(mandatory)

# Before run this code please read readme.txt file

from selenium import webdriver    #drive the web through code

mozilla_browser = webdriver.Firefox()
mozilla_browser.get('https://www.facebook.com/')

user_id = mozilla_browser.find_element_by_class_name('inputtext')

user_id.send_keys('Type your registered email_id or phone number')
password = mozilla_browser.find_element_by_id('pass')
password.send_keys('Type your password ')
signin_button = mozilla_browser.find_element_by_name('login')
signin_button.click()