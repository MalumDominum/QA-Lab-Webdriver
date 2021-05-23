import time
import random


class PatternPage:
    def __init__(self, driver):
        self.driver = driver

    def generate_patterns_with_screenshot(self, count):
        random_pattern = self.driver.find_element_by_id('new-pattern-random')
        time.sleep(0.5)
        for i in range(count):
            random_pattern.click()
            time.sleep(0.3)
            self.driver.save_screenshot("screenshot" + str(i + 1) + ".png")
        print('Open root folder to see screenshots')

    def find_background_menu_btn(self):
        return self.driver.find_element_by_xpath('//label[@for="bg"]')

    def find_color_input(self):
        return self.driver.find_element_by_xpath('//input[@name="color"]')

    def input_random_color(self, input, count):
        r = lambda: random.randint(0, 255)
        for i in range(count):
            input.send_keys('%02X%02X%02X' % (r(), r(), r()))
            time.sleep(0.2)
            input.clear()

    def find_search_btn(self):
        return self.driver.find_element_by_xpath('//label[@for="search-opt"]')

    def find_clear_btn(self):
        return self.driver.find_element_by_xpath('//button[@id="new-pattern"]')

    def find_all_icons(self):
        return self.driver.find_elements_by_xpath('//li[@class="icon"]')
