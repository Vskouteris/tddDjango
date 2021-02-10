from selenium import webdriver
import unittest
import os

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        path =os.getcwd()+ r'\tddenv\Lib\site-packages\geckodriver.exe'
        self.browser = webdriver.Firefox(executable_path=path)

    def tearDown(self):
        self.browser.quit()

    def test_random(self):
        self.browser.get("http://localhost:8000/")
        assert "To-do" in self.browser.title,"Browser title was " + self.browser.title    




if __name__ == "__main__" :
    # visitor = NewVisitorTest()
    unittest.main(warnings='ignore')        #we call unittest.main() which launches the unittest test runner which automatically finds all test classes and methods and runs them

