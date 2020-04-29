"""
@author: Juraj Holub (xholub40)
@project ITS project
@date April 2020
"""

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from steps import browser

use_step_matcher("re")


@given('the detail page of product "iPod Nano"')
def step_impl(context):
    browser.setup(context)
    # 1 | open | / |  |
    context.driver.get("http://mys01.fit.vutbr.cz:8033/")
    # 2 | setWindowSize | 1299x741 |  |
    context.driver.set_window_size(1299, 741)
    # 3 | click | linkText=MP3 Players |  |
    context.driver.find_element(By.LINK_TEXT, "MP3 Players").click()
    # 4 | click | linkText=Show All MP3 Players |  |
    context.driver.find_element(By.LINK_TEXT, "Show All MP3 Players").click()
    # 5 | mouseOver | css=.product-layout:nth-child(1) button:nth-child(2) |  |
    element = context.driver.find_element(By.CSS_SELECTOR, ".product-layout:nth-child(1) button:nth-child(2)")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    # 6 | mouseOut | css=.product-layout:nth-child(1) button:nth-child(2) |  |
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    # 7 | click | linkText=iPod Nano |  |
    context.driver.find_element(By.LINK_TEXT, "iPod Nano").click()

@when('the user submit review of product "iPod Nano"')
def step_impl(context):
    # 8 | runScript | window.scrollTo(0,31) |  |
    context.driver.execute_script("window.scrollTo(0,31)")
    # 9 | click | linkText=Reviews (0) |  |
    context.driver.find_element(By.LINK_TEXT, "Reviews (0)").click()
    # 10 | click | id=input-name |  |
    context.driver.find_element(By.ID, "input-name").click()
    # 11 | type | id=input-name | Ferko |
    context.driver.find_element(By.ID, "input-name").send_keys("Ferko")
    # 12 | click | id=input-review |  |
    context.driver.find_element(By.ID, "input-review").click()
    # 13 | type | id=input-review | Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. |
    context.driver.find_element(By.ID, "input-review").send_keys(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    # 14 | click | css=input:nth-child(5) |  |
    context.driver.find_element(By.CSS_SELECTOR, "input:nth-child(5)").click()
    # 15 | click | id=button-review |  |
    context.driver.find_element(By.ID, "button-review").click()

@then("the user recievs information about succesfull submit")
def step_impl(context):
    context.driver.implicitly_wait(.2)
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".alert")
    assert len(elements) > 0
    value = elements[0].text
    assert value == 'Thank you for your review. It has been submitted to the webmaster for approval.'
    browser.teardown(context)


@step("the administrator recievs submitted review for approval")
def step_impl(context):
    pass # not implemented


@given("Admin login into Review submit list")
def step_impl(context):
    pass # not implemented


@when('the admin modify status of the review "iPodNano" to Enabled')
def step_impl(context):
    pass # not implemented


@then('the user sees "iPodNano" review in this product detail page')
def step_impl(context):
    pass # not implemented
