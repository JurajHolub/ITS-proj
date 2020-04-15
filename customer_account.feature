# -- FILE: features/customer_account.feature
# -- AUTHOR: Juraj Holub (xholub40)

Feature: The customer works with eshop as registered user

  Scenario: The user properly register
    Given the user is not registered
    When the user select to "Register" and fill the registration page with valid informations
    Then the registration success and the new user automaticly login

    Scenario: The user wants to register with invalid data
      Given the user is not registered
      When the user select to "Register" and fill the registration page with invalid informations
      Then the registration fail and user recievs info about incrrectly filled informations

    Scenario: The continual customer analyze his orders history
      Given the user is registerd, loged and already buy many products
      When the user selects account "Order History"
      Then the detail page with his "Order History" appears

    Scenario: The customer address customization
      Given the user is login
      When the user select the "Addres Book" from his account page and insert new address
      Then the new addres appears in address book

    Scenario: The user logout when the order is unfinished
      Given the user is login and his shopping cart contains "Nikon D300"
      When the user select to logout
      Then the home page appears

  Scenario: The user login into the unfinished order
    Given the user is logout and his account shopping cart contains "Nikon D300"
    When the user login
    Then the shopping cart still contains "Nikon D300"
