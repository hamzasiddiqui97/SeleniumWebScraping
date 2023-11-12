from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import openpyxl
from selenium.webdriver.common.by import By

path = r'C:\Users\Hamza\Desktop\Jupyter Notebook\Selenium'

url = 'https://books.toscrape.com/'

chrome_options = Options()
chrome_options.binary_location = ''