from behave import *

use_step_matcher("re")


@given('the current page is "Tablets" product category and user is loged in')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the current page is "Tablets" product category and user is loged in')


@when('the user adds the product "Samsung Galaxy Tab 10\.1" into his wish list')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the user adds the product "Samsung Galaxy Tab 10.1" into his wish list')


@then('the user navigation bar shows that "Wish List" contains "1" item')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the user navigation bar shows that "Wish List" contains "1" item')


@given('the logged user is in his "Wish List" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the logged user is in his "Wish List" page')


@when('the user adds to card product "Samsung Galaxy Tab 10\.1"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the user adds to card product "Samsung Galaxy Tab 10.1"')


@then('the shopping cart extends by the product "Samsung Galaxy Tab 10\.1"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the shopping cart extends by the product "Samsung Galaxy Tab 10.1"')


@when('the user removes the "Samsung Galaxy Tab 10\.1" from his wish list')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the user removes the "Samsung Galaxy Tab 10.1" from his wish list')


@then('the wish list does not contains product "Samsung Galaxy Tab 10\.1"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the wish list does not contains product "Samsung Galaxy Tab 10.1"')