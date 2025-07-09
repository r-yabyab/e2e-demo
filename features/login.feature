Feature: User can log in

    Scenario: User can see usernames on homepage
        Given I open the SauceDemo homepage
        Then I should see a list of users on the homepage
    
    Scenario: User can log in
        Given I open the SauceDemo homepage
        When I log in
        Then I should see the inventory page