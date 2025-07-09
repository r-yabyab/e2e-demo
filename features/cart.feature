Feature: User can add item to cart

    Scenario:
        Given I log in with Playwright
        When I add a backpack to the cart
        Then the cart icon should show "1"