# -- FILE: features/review_product.feature
# -- AUTHOR: Juraj Holub (xholub40)

Feature: Review the selected product

    Scenario: Submit review
        Given the detail page of product "iPod Nano"
        When the user submit review of product "iPod Nano"
        Then the user recievs information about succesfull submit
        And the administrator recievs submitted review for approval

    Scenario: Approve submited review
        Given Admin login into Review submit list
        When the admin modify status of the review "iPodNano" to Enabled
        Then the user sees "iPodNano" review in this product detail page
