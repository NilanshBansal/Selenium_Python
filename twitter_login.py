from selenium import webdriver
from getpass import getpass
import time

usr=input("enter your username or eail id: ")
pwd=getpass("enter your password: ")

driver= webdriver.Chrome("/Users/nilansh/Downloads/chromedriver")
driver.get("https://twitter.com/")

time.sleep(10)

username_box=driver.find_element_by_css_selector("input.text-input.email-input.js-signin-email")
username_box.send_keys(usr)

password_box=driver.find_element_by_name("session[password]")
password_box.send_keys(pwd)

login_btn=driver.find_element_by_css_selector("input.EdgeButton.EdgeButton--secondary.EdgeButton--medium.submit.js-submit")
login_btn.submit()

