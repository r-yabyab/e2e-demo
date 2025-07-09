Feature: Add to cart

    Scenario:
        Given I open the SauceDemo homepage with Playwright
        When I input username "standard_user"
        And I see "standard_user" in the login credentials section
        And I input password "secret_sauce"
        And I click the login button with Playwright
        And I see "Sauce Labs Backpack" in the inventory list
        And Inventory page is loaded
        And I click the element with selector "#add-to-cart-sauce-labs-backpack"
        Then the cart should show "1"