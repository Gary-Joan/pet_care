Feature: Testeo de historia generar cita
    In order to prove that the first history works
    As the user
    I want to test first the url element
    Scenario: see appointment page
        Given user is on login page
        When user fill "username" with "garyjoan"
        And user fill "password" with "garyjoan09"
        Then user will redirect to home page
        Given user is on home page
        When user type "cliente/" on browser
        And user type "event/new/" on browser
        Then user see "event.html" page

    Scenario: filling event form

        Given user is on event page and see login form
        When user fill "Mascota" with "max"
        And user fill "Descripcion del problema" with "dolor pierna delantera"
        And user fill "Fecha y hora a reservar" with "12/09/002019 05:44"
        Then user click con "pedir cita" option

     Scenario: logout
         Given user is on home page
         When user click on "LOGOUT" option
         Then user can see home page