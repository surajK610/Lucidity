from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# import org.openqa.selenium.WebElement
# import org.openqa.selenium.chrome.ChromeDriver
# import org.openqa.selenium.chrome.ChromeOptions
# import org.openqa.selenium.safari.SafariDriver
# import org.openqa.selenium.safari.SafariOptions
# import org.openqa.selenium.support.ui.Select

PATH = r'chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("http://localhost:3000/login")
print(driver.title)

print("TEST LOG IN BUTTON TEXT")
log_in_buttons = driver.find_elements_by_class_name("link-right")
log_in = log_in_buttons[0]
assert (log_in.text == "Log In")
print("================================")


print("TEST NEW TO LUCIDITY BUTTON TEXT")
new_to_lucidity_list = driver.find_elements_by_class_name("form-link")
new_to_lucidity = new_to_lucidity_list[0]
assert (new_to_lucidity.text != "New to Lucidity!")
assert (new_to_lucidity.text == "New to Lucidity?")
print("================================")

time.sleep(3)

print("TEST CLICKING NEW TO LUCIDITY BUTTON")
new_to_lucidity.click()
print("================================")

time.sleep(3)

print("TEST CLICKING lOG IN BUTTON AGAIN")
log_in_2 = driver.find_elements_by_class_name("form-link")[0]
log_in_2.click()
print("================================")

time.sleep(3)

print("TEST CLICKING NEW TO LUCIDITY BUTTON")
new_to_lucidity.click()
print("================================")

print("TESTING CREATING NEW ACCOUNT")
new_user_form_email = driver.find_elements_by_name("email")
print("================================")

print("TESTING THAT THE EMAIL FORM ENTRY WORKS...")
email_form = new_user_form_email[0]
assert(email_form.get_attribute('name') == "email")

email_form.send_keys("abcde@gmail.com")

print("================================")

print("STILL TESTING CREATING NEW ACCOUNT")
new_user_form_name = driver.find_elements_by_name("name")
print("================================")

print("TESTING THAT THE EMAIL FORM ENTRY WORKS...")
name_form = new_user_form_name[0]
assert(name_form.get_attribute('name') == "name")

name_form.send_keys("selenium")

print("================================")

print("TESTING ENTERING PASSWORD...")

password_box_list = driver.find_elements_by_name("pass")
password_box = password_box_list[0]
assert (password_box.get_attribute('name') == "pass")

password_box.send_keys("password12345")

print("================================")

print("TESTING PRESSING SUBMIT")

form_container_list = driver.find_elements_by_class_name("form-container")
form_container = form_container_list[0]

print("================================")

time.sleep(5)

print("QUITTING...")
driver.quit()

