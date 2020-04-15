# -- FILE: features/product_comparison.feature
# -- AUTHOR: Juraj Holub (xholub40)

Feature: The products comparison

    Scenario: Add the first product to comparison
        Given the "Phones & PDAs" products shows on the eshop 
        When the user choose to "Compare This Product" to "iPhone" product at the page
        Then the notification appears about the "iPhone" comparison

    Scenario: Add the second product to comparison
        Given the "iPhone" product is in the product comparison
        When the user add product "HTC Touch HD" into comparison
        Then the notification about the product comparison of the "HTC Touch HD" appears

    Scenario: Comparsion of the two products
        Given the "iPhone" and "HTC Touch HD" are in comparison
        When the user choose the "Product Compare(2)" option
        Then the product comparison of the "iPhone" and "HTC Touch HD" appears

    Scenario: Add the third product to comparison
        Given the "Phones & PDAs" products shows on the eshop
        When the user add product "Palm Tree Pro" into comparison
        Then the notification about the product comparison of the "Palm Tree Pro" appears

    Scenario: Details comparsion products
        Given the "iPhone", "HTC Touch HD" and "Palm Tree Pro" are in comparison
        When the user select "Product Compare" option
        Then the detail page with comparsion details of the "iPhone", "HTC Touch HD" and "Palm Tree Pro" appears

    Scenario: User wants to compare too many products
        Given the "iPhone", "HTC Touch HD", "Palm Tree Pro" and "Nikon D300" are in comparison
        When the user add "Samsung Galaxy Tab 10.1" into comparison
        Then the "Samsung Galaxy Tab 10.1" replaces the oldest comparison product
