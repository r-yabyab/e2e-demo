Feature: SauceDemo login

    Scenario: Check login credentials text on homepage
        Given I open the SauceDemo homepage
        Then I should see "standard_user" in the login credentials section
    
    Scenario: Successful login
        Given I open the SauceDemo homepage
        When I enter username "standard_user"
        And I enter password "secret_sauce"
        And I click the login button
        Then I should be logged in successfully