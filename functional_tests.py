from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\Users\user\Documents\Python Scripts\TDD\tddenv\Lib\site-packages\geckodriver.exe')
browser.get("http://localhost:8000/")

assert "Django" in browser.title


