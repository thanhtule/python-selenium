# Automation test
- Using [Selenium](https://www.selenium.dev/).
- Language: [Python](https://www.python.org/).

## Refer link
- https://pypi.org/project/selenium/
- https://docs.python.org/3/library/unittest.html

## Download web driver
- [Chrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [Edge driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- [Firefox driver](https://github.com/mozilla/geckodriver/releases)
- [Safari driver](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

## Install Firefox binary
- sudo apt-get install libdbus-glib-1-2
- sudo apt-get install libxt6

## Install Chrome binary

## Install project
- Clone source code from Gitlab
  ```
  git clone http://10.20.10.20/development/wysebone-auto-test.git /path/to/project
  or
  git clone --branch <branchname> http://10.20.10.20/development/wysebone-auto-test.git /path/to/project
  ```
- Project configuration
  Config the project by setting default values in the .env file.
  ```
  DEBUG=False

  # Web driver
  CHROME_DRIVER=/path/to/webdriver/chromedriver
  EDGE_DRIVER=/path/to/webdriver/msedgedriver
  FIREFOX_DRIVER=/path/to/webdriver/geckodriver
  IE_DRIVER=/path/to/webdriver/iedriver
  ```

## Install package
```
python -m pip install -r requirements.txt
```

## Command-Line Interface
```
python -m unittest test_module1 test_module2 -v
python -m unittest test_module.TestClass -v
python -m unittest test_module.TestClass.test_method -v
```

## Test Discovery
```
python -m unittest discover tests "*_test.py" -v
```

or

```
nohup sh runtest.sh > /var/www/autotest/logs/auto-x.x.x.log 2>&1 &
```


## Example
### Example 0:
- Open a new Firefox browser
- Load the page at the given URL

```py
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://seleniumhq.org/')
```

### Example 1:
- Open a new Firefox browser
- Load the Yahoo homepage
- Search for “seleniumhq”
- Close the browser

```py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

# assert 'Yahoo' in browser.title
browser.get('http://www.yahoo.com')

# Find the search box
elem = browser.find_element_by_name('p')
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()
```

### Example 2: Selenium with unittest
- Selenium WebDriver + Unittest

```py
import unittest
from libs import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.load_chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main()
```
