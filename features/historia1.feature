Feature: Testeo de historia 1
    In order to prove that the first history works
    As the developer
    I want to test first the url element

    Scenario: The Url Test for the new date appointnment
        Given user in on "client.html" page
        When user clink on "pedir cita"
        then the app show "event.html" page to create an appointment

    Scenario: client creates a new appointment
        Given client is "event.html" to create new appoitn
        when user input "max" as pet name,
        and "dolor pierna" as illness description
        and "7/8/19" as appointmente date
        and click "pedir cita"
        then appointmen is created and user is on "client.hmtl" page


