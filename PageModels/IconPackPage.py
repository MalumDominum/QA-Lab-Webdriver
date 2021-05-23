class IconPackPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.set_window_size(1920, 1080, self.driver.window_handles[0])

    def find_pattern_link(self):
        return self.driver.find_element_by_xpath(
            '//a[@class="bj-button bj-button--secondary btn-pattern fullwidth alignc '
            'tooltip__trigger tooltip__trigger--disabled tooltip--bottom-right "]')

    def change_target_on(self, value, target):
        self.driver.execute_script('arguments[0].setAttribute("target", ' + target + ')', value)
