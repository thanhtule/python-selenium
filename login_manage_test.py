import unittest

from selenium.webdriver.chrome.webdriver import WebDriver
from libs import webdriver, xml
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Login_Manage(unittest.TestCase):    

    def setUp(self):
        self.browser = webdriver.load_driver()
        self.addCleanup(self.browser.quit)

        self.data = xml.getdata('data_login_manage.xml')
        url = self.data['wysebone']['url']
        self.browser.get(url)
        self.browser.implicitly_wait(5)
        self.browser.maximize_window()
  

    def test_login_success(self): 

        print('To test login success')

        email = self.data['wysebone']['data-1']['email']
        password = self.data['wysebone']['data-1']['password']
        language = self.data['wysebone']['language'] 
        en_mess =  self.data['wysebone']['message']['success']['en']
        ja_mess =  self.data['wysebone']['message']['success']['ja']
        vi_mess =  self.data['wysebone']['message']['success']['vi']
    
        # Change languages
        select = Select(self.browser.find_element_by_id('language_id'))
        select.select_by_value(language)
    
        # Find email element in login page
        email_element = self.browser.find_element_by_id('id_email')

        # Set value for email element
        email_element.send_keys(email)

        # Find password element in login page
        pass_element = self.browser.find_element_by_id('id_password')

        # Set value for password element
        pass_element.send_keys(password)

        # Submit form
        pass_element.send_keys(Keys.ENTER)

        if language == 'en':
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH,'//*[@id="user-tools"]'))
                )
            
            # Test the title page is "Site administration | Dynash"    
            self.assertIn(en_mess, self.browser.title)

        elif language == 'ja':
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH,'//*[@id="user-tools"]'))
                )

            # Test the title page is "サイト管理 | Dynash"    
            self.assertIn(ja_mess, self.browser.title)

        else:

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH,'//*[@id="user-tools"]'))
                )
            # Test the title page is "Site quản trị hệ thống. | Dynash"
            self.assertIn(vi_mess, self.browser.title)

        # log out
        self.browser.find_element_by_xpath('//*[@id="user-tools"]/a[3]').click()

    def test_login_empty(self):
        
        print('To test login with Email/Password is empty')

        # check disable button
        button = self.browser.find_element_by_xpath('//*[@id="login-form"]/button')
        self.browser.execute_script("arguments[0].setAttribute('disabled','true')", button)

    def test_login_empty_pass(self):

        print('To test login with Password is empty')

        email = self.data['wysebone']['data-2']['email']        
            
        # Find email element in login page
        email_element = self.browser.find_element_by_id('id_email')

        # Set value for email element
        email_element.send_keys(email)
        

        # check disable button
        button = self.browser.find_element_by_xpath('//*[@id="login-form"]/button')
        self.browser.execute_script("arguments[0].setAttribute('disabled','true')", button)

    def test_login_empty_email(self):

        print('To test login with Email is empty')
        
        password = self.data['wysebone']['data-3']['password']
        
        # Find password element in login page
        pass_element = self.browser.find_element_by_id('id_password')

        # Set value for password element
        pass_element.send_keys(password)

        # check disable button
        button = self.browser.find_element_by_xpath('//*[@id="login-form"]/button')
        self.browser.execute_script("arguments[0].setAttribute('disabled','true')", button)

    def test_login_invalid_email(self): 

        print('To test login with Email invalid')

        email = self.data['wysebone']['data-4']['email']
        password = self.data['wysebone']['data-4']['password']
        language = self.data['wysebone']['language']  
        en_fail =  self.data['wysebone']['message']['failed']['en']
        ja_fail =  self.data['wysebone']['message']['failed']['ja']
        vi_fail =  self.data['wysebone']['message']['failed']['vi']
    
        # Change languages
        select = Select(self.browser.find_element_by_id('language_id'))
        select.select_by_value(language)
    
        # Find email element in login page
        email_element = self.browser.find_element_by_id('id_email')

        # Set value for email element
        email_element.send_keys(email)

        # Find password element in login page
        pass_element = self.browser.find_element_by_id('id_password')

        # Set value for password element
        pass_element.send_keys(password)

        # Submit form
        pass_element.send_keys(Keys.ENTER)

        if language == 'en':
            
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]//div[1]').text

            # Test the message error    
            self.assertIn(en_fail, mess_error)

        elif language == 'ja':
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(ja_fail, mess_error)

        else:

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(vi_fail, mess_error)

    def test_login_invalid_pass(self): 

        print('To test login with Password invalid')

        email = self.data['wysebone']['data-5']['email']
        password = self.data['wysebone']['data-5']['password']
        language = self.data['wysebone']['language']  
        en_fail =  self.data['wysebone']['message']['failed']['en']
        ja_fail =  self.data['wysebone']['message']['failed']['ja']
        vi_fail =  self.data['wysebone']['message']['failed']['vi']

        # Change languages
        select = Select(self.browser.find_element_by_id('language_id'))
        select.select_by_value(language)
    
        # Find email element in login page
        email_element = self.browser.find_element_by_id('id_email')

        # Set value for email element
        email_element.send_keys(email)

        # Find password element in login page
        pass_element = self.browser.find_element_by_id('id_password')

        # Set value for password element
        pass_element.send_keys(password)

        # Submit form
        pass_element.send_keys(Keys.ENTER)

        if language == 'en':
            
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]//div[1]').text

            # Test the message error    
            self.assertIn(en_fail, mess_error)

        elif language == 'ja':
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(ja_fail, mess_error)

        else:

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(vi_fail, mess_error)

    def test_login_invalid_email_pass(self): 

        print('To test login with Email/Password invalid')

        email = self.data['wysebone']['data-6']['email']
        password = self.data['wysebone']['data-6']['password']
        language = self.data['wysebone']['language']  
        en_fail =  self.data['wysebone']['message']['failed']['en']
        ja_fail =  self.data['wysebone']['message']['failed']['ja']
        vi_fail =  self.data['wysebone']['message']['failed']['vi']
        
        # Change languages
        select = Select(self.browser.find_element_by_id('language_id'))
        select.select_by_value(language)
    
        # Find email element in login page
        email_element = self.browser.find_element_by_id('id_email')

        # Set value for email element
        email_element.send_keys(email)

        # Find password element in login page
        pass_element = self.browser.find_element_by_id('id_password')

        # Set value for password element
        pass_element.send_keys(password)

        # Submit form
        pass_element.send_keys(Keys.ENTER)

        if language == 'en':
            
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]//div[1]').text

            # Test the message error    
            self.assertIn(en_fail, mess_error)

        elif language == 'ja':
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(ja_fail, mess_error)

        else:

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(vi_fail, mess_error)

    def test_login_uppercase_lowercase_email(self): 

        print('To test login with Email uppercase/lowercase')

        email = self.data['wysebone']['data-1']['email']
        password = self.data['wysebone']['data-1']['password']
        language = self.data['wysebone']['language']  
        en_fail =  self.data['wysebone']['message']['failed']['en']
        ja_fail =  self.data['wysebone']['message']['failed']['ja']
        vi_fail =  self.data['wysebone']['message']['failed']['vi']

        # Change languages
        select = Select(self.browser.find_element_by_id('language_id'))
        select.select_by_value(language)
    
        # Find email element in login page
        email_element = self.browser.find_element_by_id('id_email')

        # Set value for email element
        email_element.send_keys(email.swapcase())

        # Find password element in login page
        pass_element = self.browser.find_element_by_id('id_password')

        # Set value for password element
        pass_element.send_keys(password)

        # Submit form
        pass_element.send_keys(Keys.ENTER)

        if language == 'en':
            
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]//div[1]').text

            # Test the message error    
            self.assertIn(en_fail, mess_error)

        elif language == 'ja':
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(ja_fail, mess_error)

        else:

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(vi_fail, mess_error)

    def test_login_uppercase_lowercase_pass(self): 

        print('To test login with Password uppercase/lowercase')

        email = self.data['wysebone']['data-1']['email']
        password = self.data['wysebone']['data-1']['password']
        language = self.data['wysebone']['language'] 
        en_fail =  self.data['wysebone']['message']['failed']['en']
        ja_fail =  self.data['wysebone']['message']['failed']['ja']
        vi_fail =  self.data['wysebone']['message']['failed']['vi'] 
    
        # Change languages
        select = Select(self.browser.find_element_by_id('language_id'))
        select.select_by_value(language)
    
        # Find email element in login page
        email_element = self.browser.find_element_by_id('id_email')

        # Set value for email element
        email_element.send_keys(email)

        # Find password element in login page
        pass_element = self.browser.find_element_by_id('id_password')

        # Set value for password element
        pass_element.send_keys(password.swapcase())

        # Submit form
        pass_element.send_keys(Keys.ENTER)

        if language == 'en':
            
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]//div[1]').text

            # Test the message error    
            self.assertIn(en_fail, mess_error)

        elif language == 'ja':
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(ja_fail, mess_error)

        else:

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(vi_fail, mess_error)

    def test_login_uppercase_lowercase_email_pass(self): 

        print('To test login with Email/Password uppercase/lowercase')

        email = self.data['wysebone']['data-1']['email']
        password = self.data['wysebone']['data-1']['password']
        language = self.data['wysebone']['language'] 
        en_fail =  self.data['wysebone']['message']['failed']['en']
        ja_fail =  self.data['wysebone']['message']['failed']['ja']
        vi_fail =  self.data['wysebone']['message']['failed']['vi'] 
    
        # Change languages
        select = Select(self.browser.find_element_by_id('language_id'))
        select.select_by_value(language)
    
        # Find email element in login page
        email_element = self.browser.find_element_by_id('id_email')

        # Set value for email element
        email_element.send_keys(email.swapcase())

        # Find password element in login page
        pass_element = self.browser.find_element_by_id('id_password')

        # Set value for password element
        pass_element.send_keys(password.swapcase())

        # Submit form
        pass_element.send_keys(Keys.ENTER)

        if language == 'en':
            
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]//div[1]').text

            # Test the message error    
            self.assertIn(en_fail, mess_error)

        elif language == 'ja':
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(ja_fail, mess_error)

        else:

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(vi_fail, mess_error)
   
    def test_login_with_space_email(self):

        print('To test login with space at the beginning or ending of Email address')

        email = self.data['wysebone']['data-7']['email']
        password = self.data['wysebone']['data-7']['password']
        language = self.data['wysebone']['language']  
        en_mess =  self.data['wysebone']['message']['success']['en']
        ja_mess =  self.data['wysebone']['message']['success']['ja']
        vi_mess =  self.data['wysebone']['message']['success']['vi']
    
        # Change languages
        select = Select(self.browser.find_element_by_id('language_id'))
        select.select_by_value(language)
    
        # Find email element in login page
        email_element = self.browser.find_element_by_id('id_email')

        # Set value for email element
        email_element.send_keys(email)

        # Find password element in login page
        pass_element = self.browser.find_element_by_id('id_password')

        # Set value for password element
        pass_element.send_keys(password)

        # Submit form
        pass_element.send_keys(Keys.ENTER)

        if language == 'en':
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH,'//*[@id="user-tools"]'))
                )
            
            # Test the title page is "Site administration | Dynash"    
            self.assertIn(en_mess, self.browser.title)

        elif language == 'ja':
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH,'//*[@id="user-tools"]'))
                )

            # Test the title page is "サイト管理 | Dynash"    
            self.assertIn(ja_mess, self.browser.title)

        else:

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH,'//*[@id="user-tools"]'))
                )
            # Test the title page is "Site quản trị hệ thống. | Dynash"
            self.assertIn(vi_mess, self.browser.title)

    def test_login_with_space_pass(self): 

        print('To test login with space at the beginning or ending of Password')

        email = self.data['wysebone']['data-8']['email']
        password = self.data['wysebone']['data-8']['password']
        language = self.data['wysebone']['language']
        en_fail =  self.data['wysebone']['message']['failed']['en']
        ja_fail =  self.data['wysebone']['message']['failed']['ja']
        vi_fail =  self.data['wysebone']['message']['failed']['vi']  
    
        # Change languages
        select = Select(self.browser.find_element_by_id('language_id'))
        select.select_by_value(language)
    
        # Find email element in login page
        email_element = self.browser.find_element_by_id('id_email')

        # Set value for email element
        email_element.send_keys(email)

        # Find password element in login page
        pass_element = self.browser.find_element_by_id('id_password')

        # Set value for password element
        pass_element.send_keys(password)

        # Submit form
        pass_element.send_keys(Keys.ENTER)

        if language == 'en':
            
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]//div[1]').text

            # Test the message error    
            self.assertIn(en_fail, mess_error)

        elif language == 'ja':
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(ja_fail, mess_error)

        else:

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(vi_fail, mess_error)

    def test_login_with_space_email_pass(self): 

        print('To test login with space at the beginning or ending of Email address and Password')

        email = self.data['wysebone']['data-9']['email']
        password = self.data['wysebone']['data-9']['password']
        language = self.data['wysebone']['language'] 
        en_fail =  self.data['wysebone']['message']['failed']['en']
        ja_fail =  self.data['wysebone']['message']['failed']['ja']
        vi_fail =  self.data['wysebone']['message']['failed']['vi'] 
    
        # Change languages
        select = Select(self.browser.find_element_by_id('language_id'))
        select.select_by_value(language)
    
        # Find email element in login page
        email_element = self.browser.find_element_by_id('id_email')

        # Set value for email element
        email_element.send_keys(email)

        # Find password element in login page
        pass_element = self.browser.find_element_by_id('id_password')

        # Set value for password element
        pass_element.send_keys(password)

        # Submit form
        pass_element.send_keys(Keys.ENTER)

        if language == 'en':
            
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]//div[1]').text

            # Test the message error    
            self.assertIn(en_fail, mess_error)

        elif language == 'ja':
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(ja_fail, mess_error)

        else:

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(vi_fail, mess_error)

    def test_login_SQL_injection_email(self): 

        print('To test login with Email address that is SQL injection')

        email = self.data['wysebone']['data-10']['email']
        password = self.data['wysebone']['data-10']['password']
        language = self.data['wysebone']['language'] 
        en_fail =  self.data['wysebone']['message']['failed']['en']
        ja_fail =  self.data['wysebone']['message']['failed']['ja']
        vi_fail =  self.data['wysebone']['message']['failed']['vi'] 
    
        # Change languages
        select = Select(self.browser.find_element_by_id('language_id'))
        select.select_by_value(language)
    
        # Find email element in login page
        email_element = self.browser.find_element_by_id('id_email')

        # Set value for email element
        email_element.send_keys(email)

        # Find password element in login page
        pass_element = self.browser.find_element_by_id('id_password')

        # Set value for password element
        pass_element.send_keys(password)

        # Submit form
        pass_element.send_keys(Keys.ENTER)

        if language == 'en':
            
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]//div[1]').text

            # Test the message error    
            self.assertIn(en_fail, mess_error)

        elif language == 'ja':
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(ja_fail, mess_error)

        else:

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(vi_fail, mess_error)

    def test_login_SQL_injection_pass(self): 

        print('To test login with Password that is SQL injection')

        email = self.data['wysebone']['data-11']['email']
        password = self.data['wysebone']['data-11']['password']
        language = self.data['wysebone']['language'] 
        en_fail =  self.data['wysebone']['message']['failed']['en']
        ja_fail =  self.data['wysebone']['message']['failed']['ja']
        vi_fail =  self.data['wysebone']['message']['failed']['vi'] 
    
        # Change languages
        select = Select(self.browser.find_element_by_id('language_id'))
        select.select_by_value(language)
    
        # Find email element in login page
        email_element = self.browser.find_element_by_id('id_email')

        # Set value for email element
        email_element.send_keys(email)

        # Find password element in login page
        pass_element = self.browser.find_element_by_id('id_password')

        # Set value for password element
        pass_element.send_keys(password)

        # Submit form
        pass_element.send_keys(Keys.ENTER)

        if language == 'en':
            
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]//div[1]').text

            # Test the message error    
            self.assertIn(en_fail, mess_error)

        elif language == 'ja':
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(ja_fail, mess_error)

        else:

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(vi_fail, mess_error)

    def test_login_SQL_injection_email_pass(self): 

        print('To test login with Email address and Password that are SQL injection')

        email = self.data['wysebone']['data-12']['email']
        password = self.data['wysebone']['data-12']['password']
        language = self.data['wysebone']['language']  
        en_fail =  self.data['wysebone']['message']['failed']['en']
        ja_fail =  self.data['wysebone']['message']['failed']['ja']
        vi_fail =  self.data['wysebone']['message']['failed']['vi']
    
        # Change languages
        select = Select(self.browser.find_element_by_id('language_id'))
        select.select_by_value(language)
    
        # Find email element in login page
        email_element = self.browser.find_element_by_id('id_email')

        # Set value for email element
        email_element.send_keys(email)

        # Find password element in login page
        pass_element = self.browser.find_element_by_id('id_password')

        # Set value for password element
        pass_element.send_keys(password)

        # Submit form
        pass_element.send_keys(Keys.ENTER)

        if language == 'en':
            
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]//div[1]').text

            # Test the message error    
            self.assertIn(en_fail, mess_error)

        elif language == 'ja':
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(ja_fail, mess_error)

        else:

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH,'//*[@id="login-form"]/div[1]/button'))
                )

            mess_error = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[1]').text
            
            # Test the message error    
            self.assertIn(vi_fail, mess_error)

    def tearDown(self):
        self.browser.close()

def suite():
    tests = [
        'test_login_success', 
        'test_login_empty',
        'test_login_empty_pass',
        'test_login_empty_email',
        'test_login_invalid_email',
        'test_login_invalid_pass',
        'test_login_invalid_email_pass',
        'test_login_uppercase_lowercase_email',
        'test_login_uppercase_lowercase_pass',
        'test_login_uppercase_lowercase_email_pass',
        'test_login_with_space_email',
        'test_login_with_space_pass',
        'test_login_with_space_email_pass',
        'test_login_SQL_injection_email',
        'test_login_SQL_injection_pass',
        'test_login_SQL_injection_email_pass'
    ]
    return unittest.TestSuite(map(Login_Manage, tests))






