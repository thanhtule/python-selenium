from decouple import config
from selenium import webdriver
from libs import settings


def load_chrome():
    try:
        driver = config('CHROME_DRIVER', default='')
        return webdriver.Chrome(executable_path=driver)
    except BaseException:
        raise BaseException('Invalid Chrome driver.')
    

def load_edge():
    try:
        driver = config('EDGE_DRIVER', default='')
        return webdriver.Edge(executable_path=driver)
    except BaseException as error:
        print(error)
        raise BaseException('Invalid Edge driver.')
    

def load_firefox():
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

    try:
        driver = config('FIREFOX_DRIVER', default='')

        if settings.FIREFOX_BINARY:
            options = Options()
            options.add_argument("--headless")
            binary = FirefoxBinary(settings.FIREFOX_BINARY)
            return webdriver.Firefox(executable_path=driver, options=options, firefox_binary=binary)

        return webdriver.Firefox(executable_path=driver)
    except BaseException as error:
        print(error)
        raise BaseException('Invalid Firefox driver.')

    
def load_driver():
    """Load web driver
    """

    if settings.DEFAULT_DRIVER == 'CHROME':
        return load_chrome()
    
    if settings.DEFAULT_DRIVER == 'EDGE':
        return load_edge()
    
    return load_firefox()
