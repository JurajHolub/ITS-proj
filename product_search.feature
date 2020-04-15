# -- FILE: features/product_search.feature
# -- AUTHOR: Juraj Holub (xholub40)

Feature: The user search for the specific product

    Scenario: Find notebook products
        Given the web browser is at the eshop home page 
        When the user chooses to show all "Laptops & Notebooks" from the product categories bar
        Then the all "Laptops & Notebooks" products shows on the eshop

    Scenario: Customize products visual display
        Given the all "Laptops & Notebooks" products shows on the eshop 
        When the user changes the items view style from "Grid" into "List"
        Then the items aligns below

    Scenario: Sort product by price
        Given the all "Laptops & Notebooks" products align belows
        When the user sort products by "Price(High > Low)"
        Then the reordered products starts with the "MacBook Pro"

    Scenario: Details of the specific product
        Given the all "Laptops & Notebooks" products shows on the eshop 
        When the user select the "MackBook Air" product
        Then the "MackBook Air" detail page appears
