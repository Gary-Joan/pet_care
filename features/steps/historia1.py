
from behave import given, when, then



@when(u'I visit Url "{url}"')
def step_impl(context, url):
    # save response in context for next step
    context.response = context.test.client.get(url)



