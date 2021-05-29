"""Revisions
 21 Feb 2021; 10:36pm; Initial creation. To download pdfs from each page.
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from scrape_tools import ScrapeTools, FormatSTF
import re
from datetime import datetime
import numpy as np

chromeOptions = webdriver.ChromeOptions()

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"download.default_directory": "C:\GitCloneDir\Final_Project\data", #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})


driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', options=options)  # Chrome driver

df = pd.read_csv(r'C:\GitCloneDir\Final_Project\data\fralib_href_list3_manualedit.csv')
print(df.head())
dload_cnt = 0

for pdf in df["url"]:
    dload_url = pdf
    dload_cnt += 1
    print("download no..." + str(dload_cnt))
    driver.get(dload_url)
    time.sleep(3)

