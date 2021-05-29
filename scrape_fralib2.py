"""Revisions
 08 Feb 2021; 11:12pm; Initial creation.
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from scrape_tools import ScrapeTools, FormatSTF
import re
from datetime import datetime
import numpy as np

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')  # Chrome driver

df = pd.read_csv(r'C:\GitCloneDir\Final_Project\data\fralib_href_list_manualedit.csv')
print(df.head())

for x in df["url"]:
    dload_url = 'https://railroads.dot.gov' + x

    print("open url...")
    driver.get(dload_url)
    time.sleep(3)

    print("get html data...")
    bs = BeautifulSoup(driver.page_source, "lxml")  # get html data from url
    list = bs.find_all('a', href=True)  # find list
    print("printing list...")

    href_list = []
    for tag in list:
        href_list.append(tag.get('href'))

    print("place in df...")
    df_href = pd.DataFrame(href_list)
    df_href = df_href.rename({0: 'url'}, axis=1)

    print(df_href)

    print("saving to csv...")
    if x == 0:
        df_href.to_csv(r"C:\GitCloneDir\Final_Project\data\fralib_href_list2.csv")  # save to CSV
    else:
        df_href.to_csv(r"C:\GitCloneDir\Final_Project\data\fralib_href_list2.csv", mode='a', header=False)  # save to CSV

