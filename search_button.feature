# -- FILE: features/search_button.feature
# -- AUTHOR: Juraj Holub (xholub40)

Feature: Search products by the search button

    Scenario: Search general products by category
        Given the home page of the eshop
        When the user search for the "Tablets" in search button
        Then The eshop shows all products in category "Tablets"

    Scenario: Search specific product by label
        Given the home page of the eshop
        When the user search for the "MacBook Air" in search button
        Then The eshop shows single product "MacBook Air"

    Scenario: Search products brand
        Given the home page of the eshop
        When the user search for the "Apple" in search button
        Then The eshop shows all "Apple" brand products that are available

    Scenario: Search witout input string
        Given the home page of the eshop
        When the user push search button witout any key words
        Then nothing happens
