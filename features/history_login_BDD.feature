Feature: login
    in order to prove that login works
    as the user
    I want to log successfully
    Scenario: see login page
        Given user is on home page
        When user click on "LOGIN"
        And user click on  "LOGIN CLIENTE"
        Then user can see login page

    Scenario: input good data in login
      Given user is on login page
      When user fill "username" with "garyjoan"
      And user fill "password" with "garyjoan09"
      Then user will redirect to home page