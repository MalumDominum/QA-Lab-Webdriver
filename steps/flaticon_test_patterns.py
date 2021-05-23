from behave import given, when, then


@given('I\'m on Flaticon main page')
def step_impl(context):
    context.main_page.open_site()


@when('I click on first non-premium icon pack')
def step_impl(context):
    context.main_page.search_non_premium_pack().click()


@then("The icon pack page opens")
def step_impl(context):
    context.scenario.skip(reason='Automatically response')


@given("I'm on icon pack page")
def step_impl(context):
    context.scenario.skip(reason='Automatically response')


@when('I change the button\'s target attribute on "{target}"')
def step_impl(context, target):
    pattern_link = context.icon_pack_page.find_pattern_link()
    context.icon_pack_page.change_target_on(pattern_link, target)
    pattern_link.click()



"""@then('Page for creating patterns is opened in same tab')
def step_impl(context, error):
    assert context.github_po.get_after_login_error() == error


@given("I'm on creating pattern page")
def step_impl(context):
    context.github_po.star_click()


@when('I click on "Random pattern" button')
def step_impl(context, title):
    assert context.github_po.get_title() == title"""
