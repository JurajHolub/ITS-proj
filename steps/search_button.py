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

use_step_matcher("re")


@given("the home page of the eshop")
def step_impl(context):
    browser.setup(context)
    context.driver.get("http://mys01.fit.vutbr.cz:8033/")
    context.driver.set_window_size(1299, 741)

@when('the user search for the "Tablets" in search button')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("Tablets")
    context.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)


@then('The eshop shows all products in category "Tablets"')
def step_impl(context):
    assert context.driver.current_url == 'http://mys01.fit.vutbr.cz:8033/index.php?route=product/search&search=Laptop'
    value = context.driver.find_element(By.CSS_SELECTOR, "p:nth-child(7)").get_attribute("value")
    assert value != "There is no product that matches the search criteria."
    browser.teardown(context)


@then('The eshop shows single product "MacBook Air"')
def step_impl(context):
    assert context.driver.current_url == 'http://mys01.fit.vutbr.cz:8033/index.php?route=product/search&search=Laptop'
    value = context.driver.find_element(By.CSS_SELECTOR, "p:nth-child(7)").get_attribute("value")
    assert value != "There is no product that matches the search criteria."
    browser.teardown(context)


@then('The eshop shows all "Apple" brand products that are available')
def step_impl(context):
    assert context.driver.current_url == 'http://mys01.fit.vutbr.cz:8033/index.php?route=product/search&search=Laptop'
    value = context.driver.find_element(By.CSS_SELECTOR, "p:nth-child(7)").get_attribute("value")
    assert value != "There is no product that matches the search criteria."
    browser.teardown(context)


@when("the user push search button witout any key words")
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("")
    context.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)


@then("nothing happens")
def step_impl(context):
    assert context.driver.current_url == 'http://mys01.fit.vutbr.cz:8033/index.php?route=common/home'
    browser.teardown(context)


@when('the user search for the "MacBook Air" in search button')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("MacBook Air")
    context.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)


@when('the user search for the "Apple" in search button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "logo .img-responsive").send_keys("Apple")
