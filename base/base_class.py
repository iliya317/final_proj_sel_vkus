import datetime

class Base():

    def __init__(self,driver):
        self.driver = driver


    """Method Get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        return get_url

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')


    
        """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'Screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Blad2\\git_proj\\studing\\proj_selenium\\screen\\' + name_screenshot)

    
    
    """Method assert url"""

    def assert_url(self, result):
        url = self.get_current_url()
        assert url == result
        print('Good url')

        """Method uppend to the cart"""

    def chosed_product(self, dct):
        self.name_of_product = 'ss'
        while  isinstance(self.name_of_product, str):
            try:
                self.name_of_product = int(input(F'Hi there!\nChoose the number which you want to buy:\n{dct}:\n'))
            except KeyError:
                print('chose id, which possible in the list')
        
        return self.name_of_product


