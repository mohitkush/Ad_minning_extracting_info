#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings('ignore')


# In[2]:


import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
#from selenium.webdriver.firefox.options import Options
#options = Options()
#options.headless = True

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
url = "https://www.speedtest.net/"
driver.get(url)
time.sleep(15)
seq = driver.find_elements_by_xpath("//iframe[@title='3rd party ad content']")
i = 1
for i in range(len(seq)):
    driver.switch_to.default_content()
    iframe = driver.find_elements_by_xpath("//iframe[@title='3rd party ad content']")[i]
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    ad_img = soup.find_all('img')[1]['src'] #ad image
    with open("./Scraped_ads/"+url[12:18]+str(i)+'.jpg','wb') as f:
        im = requests.get(ad_img)
        f.write(im.content)
driver.switch_to.default_content()
driver.quit()


# In[ ]:




