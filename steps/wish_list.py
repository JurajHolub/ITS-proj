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
from steps import customer_account

use_step_matcher("re")


@given('the current page is "Tablets" product category and user is loged in')
def step_impl(context):
    context.execute_steps("""
        Given the user is login
    """)
    context.driver.find_element(By.LINK_TEXT, "Tablets").click()


@when('the user adds the product "Samsung Galaxy Tab 10\.1" into his wish list')
def step_impl(context):
    element = context.driver.find_element(By.CSS_SELECTOR, ".button-group > button:nth-child(2)")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    context.driver.find_element(By.CSS_SELECTOR, ".button-group > button:nth-child(2)").click()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()


@then('the user navigation bar shows that "Wish List" contains "1" item')
def step_impl(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".alert")
    assert len(elements) > 0
    value = elements[0].text
    assert value == 'Success: You have added Samsung Galaxy Tab 10.1 to your wish list!\n×'
    browser.teardown(context)


@given('the logged user is in his "Wish List" page')
def step_impl(context):
    context.execute_steps("""
        Given the current page is "Tablets" product category and user is loged in
        When the user adds the product "Samsung Galaxy Tab 10.1" into his wish list
    """)
    context.driver.get("http://mys01.fit.vutbr.cz:8033/index.php?route=account/wishlist")

@when('the user adds to card product "Samsung Galaxy Tab 10\.1"')
def step_impl(context):
    element = context.driver.find_element(By.CSS_SELECTOR, ".btn-danger:nth-child(2)")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    context.driver.find_element(By.CSS_SELECTOR, ".text-right > .btn-primary").click()
    element = context.driver.find_element(By.CSS_SELECTOR, ".text-right > .btn-primary")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()


@then('the shopping cart extends by the product "Samsung Galaxy Tab 10\.1"')
def step_impl(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".alert")
    assert len(elements) > 0
    value = elements[0].text
    assert value == 'Success: You have added Samsung Galaxy Tab 10.1 to your shopping cart!\n×'
    browser.teardown(context)

@when('the user removes the "Samsung Galaxy Tab 10\.1" from his wish list')
def step_impl(context):
    context.execute_steps("""
        When the user adds to card product "Samsung Galaxy Tab 10.1" 
    """)
    context.driver.find_element(By.CSS_SELECTOR, ".btn-danger:nth-child(2)").click()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()

@then('the wish list does not contains product "Samsung Galaxy Tab 10\.1"')
def step_impl(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".alert")
    assert len(elements) > 0
    value = elements[0].text
    assert value == 'Success: You have modified your wish list!\n×'
    browser.teardown(context)
