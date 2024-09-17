from Tests.web.pages.page_base import PageBase
from Tests.web.helpers.element import Element
from munch import munchify


class CalculatorPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        self.page_elements = {
             'screen': Element('//input[@id="calculator-screen"]', self).find(),
            'key_1': Element('//button[@id="key-1"]', self).find(),
            'key_2': Element('//button[@id="key-2"]', self).find(),
            'key_3': Element('//button[@id="key-3"]', self).find(),
            'key_add': Element('//button[@id="key-add"]', self).find(),
            'key_equals': Element('//button[@id="key-equals"]', self).find(),
            'key_4': Element('//button[@id="key-4"]', self).find(),
            'key_5': Element('//button[@id="key-5"]', self).find(),
            'key_6': Element('//button[@id="key-6"]', self).find(),
            'key_subtract': Element('//button[@id="key-subtract"]', self).find(),
            'key_7': Element('//button[@id="key-7"]', self).find(),
            'key_8': Element('//button[@id="key-8"]', self).find(),
            'key_9': Element('//button[@id="key-9"]', self).find(),
            'key_multiply': Element('//button[@id="key-multiply"]', self).find(),
            'key_0': Element('//button[@id="key-0"]', self).find(),
            'key_decimal': Element('//button[@id="key-decimal"]', self).find(),
            'key_clear': Element('//button[@id="key-clear"]', self).find(),
            'key_divide': Element('//button[@id="key-divide"]', self).find(),
            'toggle_button' : Element('//button[@id="toggle-button"]', self).find(),
             'logout_button' : Element('//button[@id="logout-button"]', self).find(),
             'text_window': Element('//div[@id="text-window"]', self).find(),
              'clear_history': Element('//button[@id="clear-history"]', self).find(),
             'remote_toggle': Element('//button[@id="remote-toggle"]', self).find(),
            'history': Element('//textarea[@id="history"]', self).find(),

            
            'username': Element('//label[@id="user-name"]', self).find(),

        }

        self.elements = munchify(self.page_elements)

