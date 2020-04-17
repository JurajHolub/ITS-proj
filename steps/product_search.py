"""
@author: Juraj Holub (xholub40)
@project ITS project
@date April 2020
"""

from selenium.webdriver.common.by import By
from behave import *
from steps import browser
from selenium.webdriver.common.action_chains import ActionChains

use_step_matcher("re")


@given("the web browser is at the eshop home page")
def step_impl(context):
    browser.setup(context)
    context.driver.get("http://mys01.fit.vutbr.cz:8033/")
    context.driver.set_window_size(1299, 741)


@when('the user chooses to show all "Laptops & Notebooks" from the product categories bar')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Laptops & Notebooks").click()
    context.driver.find_element(By.LINK_TEXT, "Show All Laptops & Notebooks").click()

@then('the all "Laptops & Notebooks" products shows on the eshop')
def step_impl(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".product-layout:nth-child(1) > .product-thumb")
    assert len(elements) > 0
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".product-layout:nth-child(2) > .product-thumb")
    assert len(elements) > 0
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".product-layout:nth-child(3) > .product-thumb")
    assert len(elements) > 0
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".product-layout:nth-child(5) > .product-thumb")
    assert len(elements) > 0
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".product-layout:nth-child(4) > .product-thumb")
    assert len(elements) > 0
    browser.teardown(context)

@given('the all "Laptops & Notebooks" products shows on the eshop')
def step_impl(context):
    context.execute_steps("""
        Given the web browser is at the eshop home page 
        When the user chooses to show all "Laptops & Notebooks" from the product categories bar
    """)

@when('the user changes the items view style from "Grid" into "List"')
def step_impl(context):
    context.driver.find_element(By.ID, "list-view").click()


@then("the items aligns below")
def step_impl(context):
    first_layout = context.driver.find_elements(By.CSS_SELECTOR, ".product-layout:nth-child(1) > .product-thumb")
    first_y = first_layout[0].location['y'] + first_layout[0].rect['height']

    second_layout = context.driver.find_elements(By.CSS_SELECTOR, ".product-layout:nth-child(2) > .product-thumb")
    second_y = second_layout[0].location['y'] + first_layout[0].rect['height']

    assert first_y < second_y
    browser.teardown(context)


@given('the all "Laptops & Notebooks" products align belows')
def step_impl(context):
    context.execute_steps("""
        Given the web browser is at the eshop home page 
        When the user chooses to show all "Laptops & Notebooks" from the product categories bar
    """)


@when('the user sort products by "Price\(High > Low\)"')
def step_impl(context):
    first_layout = context.driver.find_elements(By.CSS_SELECTOR, ".product-layout:nth-child(1)")
    parent_x1 = first_layout[0].location_once_scrolled_into_view['x']
    parent_x2 = first_layout[0].location_once_scrolled_into_view['x'] + first_layout[0].rect['width']
    parent_y1 = first_layout[0].location_once_scrolled_into_view['y']
    parent_y2 = first_layout[0].location_once_scrolled_into_view['y'] + first_layout[0].rect['height']

    macbook_layout = context.driver.find_elements(By.LINK_TEXT, "MacBook Pro")
    child_x1 = macbook_layout[0].location_once_scrolled_into_view['x']
    child_x2 = macbook_layout[0].location_once_scrolled_into_view['x'] + macbook_layout[0].rect['width']
    child_y1 = macbook_layout[0].location_once_scrolled_into_view['y']
    child_y2 = macbook_layout[0].location_once_scrolled_into_view['y'] + macbook_layout[0].rect['height']

    context.mac_book_is_first = parent_x1 <= child_x1 and parent_x2 >= child_x2 and parent_y1 <= child_y1 and parent_y2 >= child_y2


@then('the reordered products starts with the "MacBook Pro"')
def step_impl(context):
    assert context.mac_book_is_first
    browser.teardown(context)


@when('the user select the "MackBook Air" product')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "MacBook Air").click()


@then('the "MackBook Air" detail page appears')
def step_impl(context):
    assert context.driver.current_url == 'http://mys01.fit.vutbr.cz:8033/index.php?route=product/product&path=18&product_id=44'
    browser.teardown(context)
