class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open_site(self):
        self.driver.get('https://www.flaticon.com/')

    def search_non_premium_pack(self):
        return self.driver.find_element_by_xpath('//div[@id="fi-latest-packs"]/article/div/'
                                                 'a[@class="track"][not(span/i[@class="icon icon--premium"])][1]')
