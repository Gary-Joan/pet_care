
from behave import given, when, then


@given(u'user in on "{page}" page')
def step_impl(context, page):
    response = context.test.client.get(page)
    context.test.assertTemplateUsed(response, 'pet_care/user/cliente.html')



@when(u'user clink on "pedir cita"')
def step_impl(context):
    pass


@then(u'the app show "event.html" page to create an appointment')
def step_impl(context):
    pass


@when(u'user clink on "pedir cita" then the url "evento/nuevo" is send it')
def step_impl(context):
    pass


@then(u'url error is showing')
def step_impl(context):
    pass


@when(u'user clink on "pedir cita" then the url "event/new" is send it')
def step_impl(context):
    pass

@then(u'"event.html" is show')
def step_impl(context):
    pass


@given(u'client is "event.html" to create new appoitn')
def step_impl(context):
    pass


@when(u'user input "max" as pet name,')
def step_impl(context):
    pass


@when(u'"dolor pierna" as illness description')
def step_impl(context):
    pass


@when(u'"7/8/19" as appointmente date')
def step_impl(context):
    pass


@when(u'click "pedir cita"')
def step_impl(context):
    pass


@then(u'appointmen is created and user is on "client.hmtl" page')
def step_impl(context):
    pass


@given(u'user on "historial" page')
def step_impl(context):
    pass


@when(u'user clink on "historial mascotas"')
def step_impl(context):
    pass


@then(u'the app show a list of the historical pet')
def step_impl(context):
    pass

