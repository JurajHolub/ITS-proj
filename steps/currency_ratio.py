"""
@author: Juraj Holub (xholub40)
@project ITS project
@date April 2020
"""

from selenium.webdriver.common.by import By
from behave import *
from steps import browser

use_step_matcher("re")


@given('the eshop shows detail page of the "iMac" product')
def step_impl(context):
    browser.setup(context)
    context.driver.get("http://mys01.fit.vutbr.cz:8033/index.php?route=product/product&manufacturer_id=8&product_id=41")
    context.old = context.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(1)").text
    context.driver.set_window_size(1299, 741)

@when('the user change currency from "\$" to "€"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-group > .btn-link").click()
    context.driver.find_element(By.NAME, "EUR").click()


@then('the price of the product is "112\.84€"')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(1)").text != context.old
    browser.teardown(context)


@when('the user change currency from "€" to "\$"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-group > .btn-link").click()
    context.driver.find_element(By.NAME, "EUR").click()
    context.old = context.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(1)").text
    context.driver.find_element(By.CSS_SELECTOR, ".btn-group > .btn-link").click()
    context.driver.find_element(By.NAME, "USD").click()


@then('the price of the product is "\$122\.00"')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(1)").text != context.old
    browser.teardown(context)
