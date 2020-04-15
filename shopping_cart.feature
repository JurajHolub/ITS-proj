# -- FILE: features/shopping_cart.feature
# -- AUTHOR: Juraj Holub (xholub40)

Feature: Add and remove the item in the shopping card

    Scenario: Select desired product
        Given the eshop is at the "Cameras" product page
        When the user adds "Nikon D300" to cart
        Then the notification appears about the "Nikon D300" in shopping cart 

    Scenario: Visit shopping cart
        Given the "Nikon D300" is in the shopping cart
        When the user view selects of the "View Cart" in the the top right detailed items bar
        Then the "Shopping Cart" details appears with single item "Nikon D300"

    Scenario: Modify product quantity in the shopping cart
        Given the "Shopping Cart" details the single product "Nikon D300"
        When the user change quantity to "3"
        Then the total price change from "$98.00" into the "$294.00"

    Scenario: Use invalid Coupon Code
        Given the "Shopping Cart" details the single product "Nikon D300"
        When the user enter invalid coupon code
        Then the notification about code invalidity appears

    Scenario: Use valid Coupon Code
        Given the "Shopping Cart" details the single product "Nikon D300"
        When the user enter valid coupon code
        Then the notification about code validity appears and discount applies to shopping cart content

    Scenario: Use invalid Gift Certificate
        Given the "Shopping Cart" details the single product "Nikon D300"
        When the user enter invalid Gift Certificate
        Then the notification about Gift Certificate invalidity appears

    Scenario: Use valid Gift Certificate
        Given the "Shopping Cart" details the single product "Nikon D300"
        When the user enter valid Gift Certificate
        Then the notification about Gift Certificate validity appears and discount applies to shopping cart content

    Scenario: Empty the shopping cart
        Given the "Shopping Cart" contains the single product
        When the user remove the single product from the "Shopping Cart"
        Then the "Shopping cart" changes to empty

    Scenario: Empty the shopping cart
        Given the "Shopping Cart" contains the single product from the the "Tablet" section
        When the user select to "Continue shopping"
        Then the "Shopping cart" page changes into "Tablet" section
