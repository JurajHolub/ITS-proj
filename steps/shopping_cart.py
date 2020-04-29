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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from steps import browser

use_step_matcher("re")

@given('the eshop is at the "Cameras" product page')
def step_impl(context):
    browser.setup(context)
    context.driver.get("http://mys01.fit.vutbr.cz:8033/")
    # 2 | setWindowSize | 1050x721 |  |
    context.driver.set_window_size(1050, 721)
    # 3 | click | linkText=Cameras |  |
    context.driver.find_element(By.LINK_TEXT, "Cameras").click()


@when('the user adds "Nikon D300" to cart')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".product-layout:nth-child(2) button:nth-child(1)").click()
    context.driver.execute_script("window.scrollTo(0,588)")


@then('the notification appears about the "Nikon D300" in shopping cart')
def step_impl(context):
    element = context.wait.until(presence_of_element_located((By.CSS_SELECTOR, ".alert")))
    value = element.text
    assert value == 'Success: You have added Nikon D300 to your shopping cart!\n×'
    browser.teardown(context)



@given('the "Nikon D300" is in the shopping cart')
def step_impl(context):
    context.execute_steps("""
        Given the eshop is at the "Cameras" product page
        When the user adds "Nikon D300" to cart
    """)


@when('the user view selects of the "View Cart" in the the top right detailed items bar')
def step_impl(context):
    context.wait.until(presence_of_element_located((By.CSS_SELECTOR, ".alert")))
    element2 = context.wait.until(presence_of_element_located((By.CSS_SELECTOR, ".alert > a:nth-child(3)")))
    element2.click()


@then('the "Shopping Cart" details appears with single item "Nikon D300"')
def step_impl(context):
    element = presence_of_element_located((By.LINK_TEXT, ".alert"))
    assert element != None
    browser.teardown(context)


@given('the "Shopping Cart" details the single product "Nikon D300"')
def step_impl(context):
    context.execute_steps("""
        Given the "Nikon D300" is in the shopping cart
        When the user view selects of the "View Cart" in the the top right detailed items bar
    """)


@when('the user change quantity to "3"')
def step_impl(context):
    element1 = context.wait.until(presence_of_element_located((By.CSS_SELECTOR, "tbody:nth-child(2) .text-left > a")))
    element1.click()
    element = context.driver.find_element(By.CSS_SELECTOR, ".btn-block .btn-primary")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    context.driver.find_element(By.NAME, "quantity[112]").send_keys("3")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-block .btn-primary").click()


@then('the total price change from "\$98\.00" into the "\$294\.00"')
def step_impl(context):
    value = context.driver.find_element(By.CSS_SELECTOR, "tbody .text-right:nth-child(6)").get_attribute("value")
    assert value == "$294.00"
    browser.teardown(context)


@when("the user enter invalid coupon code")
def step_impl(context):
    element1 = context.wait.until(presence_of_element_located((By.CSS_SELECTOR, ".panel:nth-child(1) .fa")))
    element1.click()
    e2 = context.wait.until(presence_of_element_located((By.ID, "input-coupon")))
    e2.click()
    e3 = context.wait.until(presence_of_element_located((By.ID, "input-coupon")))
    e3.send_keys("12345")
    e4 = context.wait.until(presence_of_element_located((By.ID, "button-coupon")))
    e4.click()


@then("the notification about code invalidity appears")
def step_impl(context):
    element = context.wait.until(presence_of_element_located((By.CSS_SELECTOR, ".alert")))
    value = element.text
    assert value == 'Warning: Coupon is either invalid, expired or reached its usage limit!\n×'
    browser.teardown(context)


@when("the user enter valid coupon code")
def step_impl(context):
    pass # can not implement => how to set valid coupon?!


@then("the notification about code validity appears and discount applies to shopping cart content")
def step_impl(context):
    pass # can not implement => how to set valid coupon?!


@when("the user enter invalid Gift Certificate")
def step_impl(context):
    element1 = context.wait.until(presence_of_element_located((By.CSS_SELECTOR, ".panel:nth-child(3) .fa")))
    element1.click()
    e2 = context.wait.until(presence_of_element_located((By.ID, "input-voucher")))
    e2.click()
    e3 = context.wait.until(presence_of_element_located((By.ID, "input-voucher")))
    e3.send_keys("12345")
    e4 = context.wait.until(presence_of_element_located((By.ID, "button-voucher")))
    e4.click()


@then("the notification about Gift Certificate invalidity appears")
def step_impl(context):
    element = context.wait.until(presence_of_element_located((By.CSS_SELECTOR, ".alert")))
    value = element.text
    assert value == 'Warning: Gift Certificate is either invalid or the balance has been used up!\n×'
    browser.teardown(context)


@when("the user enter valid Gift Certificate")
def step_impl(context):
    pass # can not implement => how to set valid gift certificate?!


@then("the notification about Gift Certificate validity appears and discount applies to shopping cart content")
def step_impl(context):
    pass # can not implement => how to set valid gift certificate?!


@given('the "Shopping Cart" contains the single product')
def step_impl(context):
    context.execute_steps("""
        Given the "Nikon D300" is in the shopping cart
        When the user view selects of the "View Cart" in the the top right detailed items bar
    """)


@when('the user remove the single product from the "Shopping Cart"')
def step_impl(context):
    element1 = context.wait.until(presence_of_element_located((By.CSS_SELECTOR, ".fa-times-circle")))
    element1.click()

@then('the "Shopping cart" changes to empty')
def step_impl(context):
    element = context.wait.until(presence_of_element_located((By.CSS_SELECTOR, "p:nth-child(2)")))
    assert element.text == "Your shopping cart is empty!"
    browser.teardown(context)


@given('the "Shopping Cart" contains the single product from the the "Tablet" section')
def step_impl(context):
    pass # not implemented


@when('the user select to "Continue shopping"')
def step_impl(context):
    pass # not implemented


@then('the "Shopping cart" page changes into "Tablet" section')
def step_impl(context):
    pass # not implemented
