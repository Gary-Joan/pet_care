from selenium import webdriver

class Browser(object):

    base_url = 'http://127.0.0.1:8000/'
    driver = webdriver.Chrome("C:\\Users\\gjoan\\Desktop\\analisis 1\\PROYE\\pet_care\\features\\chromedriver.exe")
    driver.implicitly_wait(10)

    def close(self):
        """
        close the webdriver instance
        """
        self.driver.quit()

    def visit(self, location=''):
        """
        navigate webdriver to different pages
        """
        url = self.base_url + location

        self.driver.get(url)

    def find_by_id(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element_by_id(selector)