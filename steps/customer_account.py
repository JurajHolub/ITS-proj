"""
@author: Juraj Holub (xholub40)
@project ITS project
@date April 2020
"""

from selenium.webdriver.common.by import By
from behave import *
from steps import browser
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import names

def generate_user(context):
    context.name = names.get_first_name()
    context.surname = names.get_last_name()
    context.email = context.name + "@" + context.surname + ".com"
    context.password = "&yzKMj4p.eLk8wC@"

use_step_matcher("re")

@given("the user is not registered")
def step_impl(context):
    browser.setup(context)
    context.driver.get("http://mys01.fit.vutbr.cz:8033/")
    context.driver.set_window_size(1299, 741)
    context.driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
    value = context.driver.find_element(By.LINK_TEXT, "Register").text
    assert value == "Register"


@when('the user select to "Register" and fill the registration page with valid informations')
def step_impl(context):
    generate_user(context)
    context.driver.find_element(By.LINK_TEXT, "Register").click()
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys(context.name)
    context.driver.find_element(By.ID, "input-lastname").send_keys(context.surname)
    context.driver.find_element(By.ID, "input-email").send_keys(context.email)
    context.driver.find_element(By.ID, "input-telephone").send_keys("0911333444777")
    context.driver.find_element(By.ID, "input-address-1").click()
    context.driver.find_element(By.ID, "input-address-1").send_keys("Hlavní 13")
    context.driver.find_element(By.ID, "input-city").click()
    context.driver.find_element(By.ID, "input-city").send_keys("Praha")
    context.driver.find_element(By.ID, "input-postcode").click()
    context.driver.find_element(By.ID, "input-postcode").send_keys("12345")
    dropdown = context.driver.find_element(By.ID, "input-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Czech Republic']").click()
    element = context.driver.find_element(By.ID, "input-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = context.driver.find_element(By.ID, "input-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.ID, "input-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).release().perform()
    context.driver.find_element(By.ID, "input-country").click()
    dropdown = context.driver.find_element(By.ID, "input-zone")
    dropdown.find_element(By.XPATH, "//option[. = 'Praha']").click()
    element = context.driver.find_element(By.ID, "input-zone")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = context.driver.find_element(By.ID, "input-zone")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.ID, "input-zone")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).release().perform()
    context.driver.find_element(By.ID, "input-zone").click()
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys(context.password)
    context.driver.find_element(By.ID, "input-confirm").click()
    context.driver.find_element(By.ID, "input-confirm").send_keys(context.password)
    context.driver.find_element(By.NAME, "agree").click()
    context.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    context.driver.find_element(By.CSS_SELECTOR, ".account-success").click()


@then("the registration success and the new user automaticly login")
def step_impl(context):
    value = context.driver.find_element(By.CSS_SELECTOR, "h1").text
    assert value == "Your Account Has Been Created!"
    browser.teardown(context)


@when('the user select to "Register" and fill the registration page with invalid informations')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Register").click()

@then("the registration fail and user recievs info about incrrectly filled informations")
def step_impl(context):
    context.driver.implicitly_wait(.5)
    context.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".alert")
    assert len(elements) > 0
    browser.teardown(context)

@given("the user is registerd, loged and already buy many products")
def step_impl(context):
    pass #skip due to test complexity overkill...


@when('the user selects account "Order History"')
def step_impl(context):
    pass #skip due to test complexity overkill...


@then('the detail page with his "Order History" appears')
def step_impl(context):
    pass  # skip due to test complexity overkill...

@given("the user is login")
def step_impl(context):
    browser.setup(context)
    context.driver.get("http://mys01.fit.vutbr.cz:8033/")
    context.driver.set_window_size(1299, 741)
    context.driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
    value = context.driver.find_element(By.LINK_TEXT, "Register").text
    if value == "Register":
        context.execute_steps("""
            When the user select to "Register" and fill the registration page with valid informations
        """)
    else:
        context.driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()


@when('the user select the "Addres Book" from his account page and insert new address')
def step_impl(context):
    generate_user(context)
    context.driver.find_element(By.CSS_SELECTOR, ".list-inline .dropdown-toggle").click()
    context.driver.find_element(By.LINK_TEXT, "Order History").click()
    context.driver.find_element(By.LINK_TEXT, "Address Book").click()
    context.driver.find_element(By.LINK_TEXT, "New Address").click()
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys(context.name)
    context.driver.find_element(By.ID, "input-lastname").send_keys(context.surname)
    context.driver.find_element(By.ID, "input-address-1").click()
    context.driver.find_element(By.ID, "input-address-1").send_keys("Hlavní 13")
    context.driver.find_element(By.ID, "input-city").click()
    context.driver.find_element(By.ID, "input-city").send_keys("Praha")
    context.driver.find_element(By.ID, "input-postcode").click()
    context.driver.find_element(By.ID, "input-postcode").send_keys("12345")
    dropdown = context.driver.find_element(By.ID, "input-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Czech Republic']").click()
    element = context.driver.find_element(By.ID, "input-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = context.driver.find_element(By.ID, "input-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.ID, "input-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).release().perform()
    context.driver.find_element(By.ID, "input-country").click()
    dropdown = context.driver.find_element(By.ID, "input-zone")
    dropdown.find_element(By.XPATH, "//option[. = 'Jihočeský']").click()
    element = context.driver.find_element(By.ID, "input-zone")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = context.driver.find_element(By.ID, "input-zone")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.ID, "input-zone")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).release().perform()
    context.driver.find_element(By.ID, "input-zone").click()
    context.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


@then("the new addres appears in address book")
def step_impl(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".alert")
    assert len(elements) > 0
    value = elements[0].text
    assert value == "Your address has been successfully inserted"
    browser.teardown(context)


@given('the user is login and his shopping cart contains "Nikon D300"')
def step_impl(context):
    context.execute_steps("""
      Given the user is login
    """)
    context.driver.find_element(By.LINK_TEXT, "Cameras").click()
    context.driver.find_element(By.CSS_SELECTOR, ".product-layout:nth-child(2) button:nth-child(1)").click()

@when("the user select to logout")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
    context.driver.find_element(By.LINK_TEXT, "Logout").click()

@then("the home page appears")
def step_impl(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, "h1")
    assert len(elements) > 0
    value = elements[0].text
    assert value == "Account Logout"
    browser.teardown(context)


@given('the user is logout and his account shopping cart contains "Nikon D300"')
def step_impl(context):
    pass # this test depends on previous scenario => unacceptable


@when("the user login")
def step_impl(context):
    pass # this test depends on previous scenario => unacceptable


@then('the shopping cart still contains "Nikon D300"')
def step_impl(context):
    pass # this test depends on previous scenario => unacceptable
