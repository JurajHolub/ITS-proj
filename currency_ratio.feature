# -- FILE: features/currency_ratio.feature
# -- AUTHOR: Juraj Holub (xholub40)

Feature: Modifiation of the currency ratio

    Scenario: Change dolar into euro
        Given the eshop shows detail page of the "iMac" product
        When the user change currency from "$" to "€"
        Then the price of the product is "112.84€"

    Scenario: Change euro into dolar
        Given the eshop shows detail page of the "iMac" product
        When the user change currency from "€" to "$"
        Then the price of the product is "$122.00"

