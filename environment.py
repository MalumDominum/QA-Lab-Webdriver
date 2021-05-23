from behave import fixture, use_fixture
from selenium import webdriver
from PageModels import MainPage, IconPackPage, PatternPage
from webdriver_manager.chrome import ChromeDriverManager


@fixture
def selenium_browser_chrome(context):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    context.main_page = MainPage.MainPage(driver)
    context.icon_pack_page = IconPackPage.IconPackPage(driver)
    context.pattern_page = PatternPage.PatternPage(driver)
    yield context
    driver.quit()


def before_all(context):
    use_fixture(selenium_browser_chrome, context)
