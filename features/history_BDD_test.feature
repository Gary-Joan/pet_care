Feature: Testeo de historia generar cita
    In order to prove that the first history works
    As the user
    I want to test first the url element

    Scenario: see appointment page
        Given user is on home page
        When user type "cliente/" on browser
        And user go the username option
        Then user click con "pedir cita" option
        Then user see "event.html" page