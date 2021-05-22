from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)
driver.get('https://www.flaticon.com/')
# found first non-premium icon pack
icon_pack = driver.find_element_by_xpath('//div[@id="fi-latest-packs"]/article/div/'
                                         'a[@class="track"][not(span/i[@class="icon icon--premium"])][1]')
icon_pack.click()

# because button not visible in mobile adaptive
driver.set_window_size(1920, 1080, driver.window_handles[0])
pattern_btn = driver.find_element_by_xpath(
    '//a[@class="bj-button bj-button--secondary btn-pattern fullwidth alignc '
    'tooltip__trigger tooltip__trigger--disabled tooltip--bottom-right "]')

driver.execute_script('arguments[0].setAttribute("target","_self")', pattern_btn)
pattern_btn.click()

# Test generating random patterns and screenshot each
random_pattern = driver.find_element_by_id('new-pattern-random')
time.sleep(0.5)
for i in range(10):
    random_pattern.click()
    time.sleep(0.3)
    driver.save_screenshot("screenshot" + str(i + 1) + ".png")
print('Open root folder to see screenshots')


# Test changing background colour
background_btn = driver.find_element_by_xpath('//label[@for="bg"]')
background_btn.click()
color_input = driver.find_element_by_xpath('//input[@name="color"]')

r = lambda: random.randint(0, 255)
for i in range(10):
    color_input.send_keys('%02X%02X%02X' % (r(), r(), r()))
    time.sleep(0.2)
    color_input.clear()

# Test manually choosing the icons
search_btn = driver.find_element_by_xpath('//label[@for="search-opt"]')
search_btn.click()

clear_btn = driver.find_element_by_xpath('//button[@id="new-pattern"]')
clear_btn.click()

icons = driver.find_elements_by_xpath('//li[@class="icon"]')
for i in range(20):
    icons[i].click()

driver.close()
