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

use_step_matcher("re")

def before_all(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())

def after_all(context):
    context.driver.quit()

###############################################################################
#    Scenario: Checkout the product from the shopping cart
###############################################################################

@given('the "Shopping Cart" contains the "Nikon D300" product')
def step_impl(context):
    before_all(context)
    context.driver.get("http://mys01.fit.vutbr.cz:8033/")
    context.driver.set_window_size(1299, 741)
    context.driver.find_element(By.LINK_TEXT, "Cameras").click()
    context.driver.find_element(By.CSS_SELECTOR, ".product-layout:nth-child(2) .hidden-xs").click()
    context.driver.execute_script("window.scrollTo(0,482)")
    assert context.driver.find_element(By.LINK_TEXT, "Nikon D300")

@when('the user select "Checkout" option of his order')
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8033/")
    context.driver.set_window_size(1299, 741)
    context.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) .hidden-xs").click()
    context.driver.find_element(By.CSS_SELECTOR, ".pull-right > .btn").click()

@then('the "Checkout" page with the six steps appears')
def step_impl(context):
    assert context.driver.current_url == 'http://mys01.fit.vutbr.cz:8033/index.php?route=checkout/checkout'
    after_all(context)


###############################################################################
#       Scenario: Checkout product as Guest
###############################################################################

@given('the  checkout shows the "Step 1"')
def step_impl(context):
    context.execute_steps("""
        Given the "Shopping Cart" contains the "Nikon D300" product
        When the user select "Checkout" option of his order
    """)

@when('the user checkout as "Guest"')
def step_impl(context):
    context.driver.implicitly_wait(.1)
    context.driver.find_element(By.CSS_SELECTOR, ".radio:nth-child(4) input").click()
    context.driver.find_element(By.ID, "button-account").click()

@then('the "Billing Details" page appears')
def step_impl(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, "#collapse-payment-address > .panel-body")
    assert len(elements) > 0
    after_all(context)

###############################################################################
#   Scenario: Select billing details for the checkout and disagree with Privaci Policy
###############################################################################

@given('the checkout shows "Billing Details" page')
def step_impl(context):
    context.execute_steps("""
        Given the  checkout shows the "Step 1"
        When the user checkout as "Guest"
    """)

@when("the user correctly fill personal details")
def step_impl(context):
    context.driver.find_element(By.ID, "input-payment-firstname").send_keys("Janko")
    context.driver.find_element(By.ID, "input-payment-lastname").send_keys("Hráško")
    context.driver.find_element(By.ID, "input-payment-email").send_keys("janko.hrasko@gmail.com")
    context.driver.find_element(By.ID, "input-payment-telephone").send_keys("0910111222333")
    context.driver.find_element(By.ID, "input-payment-address-1").send_keys("Česká 22")
    context.driver.find_element(By.CSS_SELECTOR, "#address > .form-group:nth-child(5)").click()
    context.driver.find_element(By.ID, "input-payment-city").click()
    context.driver.find_element(By.ID, "input-payment-city").send_keys("Brno")
    context.driver.find_element(By.CSS_SELECTOR, ".checkout-checkout").click()
    context.driver.find_element(By.ID, "input-payment-postcode").click()
    context.driver.find_element(By.ID, "input-payment-postcode").send_keys("61600")
    context.driver.find_element(By.CSS_SELECTOR, ".checkout-checkout").click()
    dropdown = context.driver.find_element(By.ID, "input-payment-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Cyprus']").click()
    element = context.driver.find_element(By.ID, "input-payment-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = context.driver.find_element(By.ID, "input-payment-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.ID, "input-payment-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).release().perform()
    context.driver.find_element(By.ID, "input-payment-country").click()
    context.driver.find_element(By.ID, "address").click()
    dropdown = context.driver.find_element(By.ID, "input-payment-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Czech Republic']").click()
    element = context.driver.find_element(By.ID, "input-payment-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = context.driver.find_element(By.ID, "input-payment-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.ID, "input-payment-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).release().perform()
    context.driver.find_element(By.ID, "input-payment-country").click()
    dropdown = context.driver.find_element(By.ID, "input-payment-zone")
    dropdown.find_element(By.XPATH, "//option[. = 'Jihomoravský']").click()
    element = context.driver.find_element(By.ID, "input-payment-zone")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = context.driver.find_element(By.ID, "input-payment-zone")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.ID, "input-payment-zone")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).release().perform()
    context.driver.find_element(By.ID, "input-payment-zone").click()
    context.driver.find_element(By.NAME, "shipping_address").click()
    context.driver.find_element(By.ID, "button-guest").click()


@then('the warning about the neccesarity of the "Privacy Policy" agreament apperas')
def step_impl(context):
    pass # todo: the privacy policy dissappears ?!
    after_all(context)

###############################################################################
#   Scenario: Select billing details for the checkout and agree with Privaci Policy
###############################################################################

@when('the user correctly fill personal details and agree with "Privacy Policy"')
def step_impl(context):
    context.execute_steps("""
        When the user correctly fill personal details
    """)

@then('the "Delivery" page appears')
def step_impl(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, "#collapse-shipping-address  > .panel-body")
    assert len(elements) > 0
    after_all(context)

###############################################################################
#   Scenario: Specifie the address where to deliver the order
###############################################################################

@given('the checkout shows "Delivery" page')
def step_impl(context):
    context.execute_steps("""
        Given the checkout shows "Billing Details" page
        When the user correctly fill personal details and agree with "Privacy Policy"
    """)

@when("the user select an existing address for the delivery purposes")
def step_impl(context):
    context.driver.implicitly_wait(.2)
    # 29 | type | id=input-shipping-firstname | Ferko |
    context.driver.find_element(By.ID, "input-shipping-firstname").send_keys("Ferko")
    # 30 | type | id=input-shipping-lastname | Novák |
    context.driver.find_element(By.ID, "input-shipping-lastname").send_keys("Novák")
    # 31 | click | id=input-shipping-address-1 |  |
    context.driver.find_element(By.ID, "input-shipping-address-1").click()
    # 32 | click | css=.form-horizontal > .form-group:nth-child(4) |  |
    context.driver.find_element(By.CSS_SELECTOR, ".form-horizontal > .form-group:nth-child(4)").click()
    # 33 | type | id=input-shipping-address-1 | Bernolákova 1 |
    context.driver.find_element(By.ID, "input-shipping-address-1").send_keys("Bernolákova 1")
    # 34 | click | id=input-shipping-city |  |
    context.driver.find_element(By.ID, "input-shipping-city").click()
    # 35 | click | css=.form-horizontal > .form-group:nth-child(6) |  |
    context.driver.find_element(By.CSS_SELECTOR, ".form-horizontal > .form-group:nth-child(6)").click()
    # 36 | type | id=input-shipping-city | Nezamyslice |
    context.driver.find_element(By.ID, "input-shipping-city").send_keys("Nezamyslice")
    # 37 | click | css=.form-horizontal > .form-group:nth-child(7) |  |
    context.driver.find_element(By.CSS_SELECTOR, ".form-horizontal > .form-group:nth-child(7)").click()
    # 38 | type | id=input-shipping-postcode | 12345 |
    context.driver.find_element(By.ID, "input-shipping-postcode").send_keys("12345")
    # 39 | select | id=input-shipping-country | label=Cook Islands |
    #dropdown = context.driver.find_element(By.ID, "input-shipping-country")
    #elem = dropdown.find_element(By.XPATH, "//option[. = 'Cook Islands']")
    #context.driver.implicitly_wait(.1)
    #elem.click()
    # 40 | mouseDownAt | id=input-shipping-country | -277.65625,-393 |
    element = context.driver.find_element(By.ID, "input-shipping-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 41 | mouseMoveAt | id=input-shipping-country | -277.65625,-393 |
    element = context.driver.find_element(By.ID, "input-shipping-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    # 42 | mouseUpAt | id=input-shipping-country | -277.65625,-393 |
    element = context.driver.find_element(By.ID, "input-shipping-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).release().perform()
    # 43 | click | id=input-shipping-country |  |
    # 19 | click | css=.checkout-checkout |  |
    context.driver.find_element(By.CSS_SELECTOR, ".checkout-checkout").click()
    # 20 | select | id=input-shipping-country | label=Angola |
    dropdown = Select(context.driver.find_element(By.ID, "input-shipping-country"))
    dropdown.select_by_index(1)
    # 21 | mouseDownAt | id=input-shipping-country | -277.65625,-212 |
    element = context.driver.find_element(By.ID, "input-shipping-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 22 | mouseMoveAt | id=input-shipping-country | -277.65625,-212 |
    element = context.driver.find_element(By.ID, "input-shipping-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    # 23 | mouseUpAt | id=input-shipping-country | -277.65625,-212 |
    element = context.driver.find_element(By.ID, "input-shipping-country")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).release().perform()
    # 24 | click | id=input-shipping-country |  |
    context.driver.find_element(By.ID, "input-shipping-country").click()
    # 25 | select | id=input-shipping-zone | label=Bie |
    dropdown = Select(context.driver.find_element(By.ID, "input-shipping-zone"))
    dropdown.select_by_index(1)
    # 26 | mouseDownAt | id=input-shipping-zone | -277.65625,-261 |
    element = context.driver.find_element(By.ID, "input-shipping-zone")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 27 | mouseMoveAt | id=input-shipping-zone | -277.65625,-261 |
    element = context.driver.find_element(By.ID, "input-shipping-zone")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    # 28 | mouseUpAt | id=input-shipping-zone | -277.65625,-261 |
    element = context.driver.find_element(By.ID, "input-shipping-zone")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).release().perform()
    # 29 | click | id=input-shipping-zone |  |
    context.driver.find_element(By.ID, "input-shipping-zone").click()
    context.driver.find_element(By.ID, "button-guest-shipping").click()


@then('the checkout shows "Delivery Method" page')
def step_impl(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, "#collapse-shipping-method  > .panel-body")
    assert len(elements) > 0
    after_all(context)

###############################################################################
#   Scenario: Select method of the delivery
###############################################################################

@given('the checkout shows "Delivery Method" page')
def step_impl(context):
    context.execute_steps("""
        Given the checkout shows "Delivery" page
        When the user select an existing address for the delivery purposes
    """)

@when("the user choose specific method")
def step_impl(context):
    context.driver.find_element(By.NAME, "comment").click()
    # 74 | type | name=comment | The most important comment about my order. |
    context.driver.find_element(By.NAME, "comment").send_keys("The most important comment about my order.")
    # 75 | click | id=button-shipping-method |  |
    context.driver.find_element(By.ID, "button-shipping-method").click()
    # 76 | click | id=button-guest-shipping |  |
    #context.driver.find_element(By.ID, "button-guest-shipping").click()

@then('the checkout changes into the "Payment Method" page')
def step_impl(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, "#collapse-payment-method  > .panel-body")
    assert len(elements) > 0
    after_all(context)

###############################################################################
#   Scenario: Select payment method and disagree with terms and conditions
###############################################################################

@given('the checkout shows "Payment Method" step')
def step_impl(context):
    context.execute_steps("""
        Given the checkout shows "Delivery Method" page
        When the user choose specific method
    """)

@when("the user select particular method")
def step_impl(context):
    # 79 | click | name=payment_method |  |
    context.driver.find_element(By.NAME, "payment_method").click()
    # 80 | click | css=p:nth-child(4) > .form-control |  |
    context.driver.find_element(By.CSS_SELECTOR, "p:nth-child(4) > .form-control").click()
    # 81 | click | css=html |  |
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    # 82 | type | css=p:nth-child(4) > .form-control | Add comment about my order. |
    context.driver.find_element(By.CSS_SELECTOR, "p:nth-child(4) > .form-control").send_keys("Add comment about my order.")
    # 84 | click | id=button-payment-method |  |
    context.driver.find_element(By.ID, "button-payment-method").click()

@then('the checkout warning about the necessarity of the "Terms & Conditions" agreement')
def step_impl(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".alert")
    assert len(elements) > 0
    after_all(context)

###############################################################################
#   Scenario: Select payment method and agree with terms and conditions
###############################################################################

@when('the user select particular method and agree with "Terms & Conditions"')
def step_impl(context):
    # 79 | click | name=payment_method |  |
    context.driver.find_element(By.NAME, "payment_method").click()
    # 80 | click | css=p:nth-child(4) > .form-control |  |
    context.driver.find_element(By.CSS_SELECTOR, "p:nth-child(4) > .form-control").click()
    # 81 | click | css=html |  |
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    # 82 | type | css=p:nth-child(4) > .form-control | Add comment about my order. |
    context.driver.find_element(By.CSS_SELECTOR, "p:nth-child(4) > .form-control").send_keys("Add comment about my order.")
    context.driver.find_element(By.NAME, "agree").click()
    context.driver.find_element(By.ID, "button-payment-method").click()


@then('the checkout shows "Confirm Order"')
def step_impl(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, "#collapse-checkout-confirm > .panel-body")
    assert len(elements) > 0
    after_all(context)

###############################################################################
#   Scenario: Confirm the finished order
###############################################################################

@given('the checkout shows "Confirm Order" step')
def step_impl(context):
    context.execute_steps("""
        Given the checkout shows "Payment Method" step
        When the user select particular method and agree with "Terms & Conditions"
    """)


@when("the user confirm order")
def step_impl(context):
    context.driver.find_element(By.ID, "button-confirm").click()


@then("the Shopping cart checkout shows the information about succesful order")
def step_impl(context):
    assert context.driver.current_url == 'http://mys01.fit.vutbr.cz:8033/index.php?route=checkout/success'
    after_all(context)
