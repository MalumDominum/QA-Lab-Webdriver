from behave import given, when, then


@given("I'm on Flaticon main page")
def step_impl(context):
    context.main_page.open_site()


@when('I click on first non-premium icon pack')
def step_impl(context):
    context.main_page.search_non_premium_pack.click()


