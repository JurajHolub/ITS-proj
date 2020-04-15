# -- FILE: features/wish_list.feature
# -- AUTHOR: Juraj Holub (xholub40)

Feature: Wish list of products

    Scenario: Add product to wish list
        Given the current page is "Tablets" product category and user is loged in
        When the user adds the product "Samsung Galaxy Tab 10.1" into his wish list
        Then the user navigation bar shows that "Wish List" contains "1" item

    Scenario: Add item from wish list to shopping cart
        Given the logged user is in his "Wish List" page
        When the user adds to card product "Samsung Galaxy Tab 10.1" 
        Then the shopping cart extends by the product "Samsung Galaxy Tab 10.1"

    Scenario: Remove item from wish list
        Given the logged user is in his "Wish List" page
        When the user removes the "Samsung Galaxy Tab 10.1" from his wish list
        Then the wish list does not contains product "Samsung Galaxy Tab 10.1"
