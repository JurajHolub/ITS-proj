# -- FILE: features/checkout_product.feature
# -- AUTHOR: Juraj Holub (xholub40)

Feature: Checkout the selected product

    Scenario: Checkout the product from the shopping cart
        Given the "Shopping Cart" contains the "Nikon D300" product
        When the user select "Checkout" option of his order
        Then the "Checkout" page with the six steps appears

    Scenario: Checkout product as Guest
        Given the  checkout shows the "Step 1"
        When the user checkout as "Guest"
        Then the "Billing Details" page appears

    Scenario: Select billing details for the checkout and disagree with Privaci Policy
        Given the checkout shows "Billing Details" page
        When the user correctly fill personal details
        Then the warning about the neccesarity of the "Privacy Policy" agreament apperas

    Scenario: Select billing details for the checkout and agree with Privaci Policy
        Given the checkout shows "Billing Details" page
        When the user correctly fill personal details and agree with "Privacy Policy"
        Then the "Delivery" page appears

    Scenario: Specifie the address where to deliver the order
        Given the checkout shows "Delivery" page
        When the user select an existing address for the delivery purposes
        Then the checkout shows "Delivery Method" page

    Scenario: Select method of the delivery
        Given the checkout shows "Delivery Method" page
        When the user choose specific method
        Then the checkout changes into the "Payment Method" page

    Scenario: Select payment method and disagree with terms and conditions
        Given the checkout shows "Payment Method" step
        When the user select particular method
        Then the checkout warning about the necessarity of the "Terms & Conditions" agreement

    Scenario: Select payment method and agree with terms and conditions
        Given the checkout shows "Payment Method" step
        When the user select particular method and agree with "Terms & Conditions"
        Then the checkout shows "Confirm Order"

    Scenario: Confirm the finished order
        Given the checkout shows "Confirm Order" step
        When the user confirm order
        Then the Shopping cart checkout shows the information about succesful order

