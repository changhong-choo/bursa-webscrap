from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
from datetime import datetime
import pandas as pd
import time

url = 'https://www.bursamalaysia.com/market_information/indices_prices'

dfs = []

driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)
#r = driver.page_source


for loop in range(1,3):
    r = driver.page_source
    soup = bs(r, "html.parser")
    table = soup.find('div', {'class' : 'dataTables_scroll'})
    a = table.find('table', {'id' : 'DataTables_Table_0'})
    df = pd.read_html(str(a))[0]
    dfs.append(df)
    
    if loop == 2:
        break
    else:
        button = driver.find_element_by_css_selector('[class="paginate_button page-item next"]')
        ActionChains(driver).send_keys(Keys.CONTROL + Keys.HOME).perform()
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        #driver.execute_script("arguments[0].click()", button)
        time.sleep(1)
        button.click()
        time.sleep(2)


b = pd.concat(dfs)

filename = datetime.now().strftime('bursaIndicesPrices_%Y%m%d.csv')
b.to_csv(filename, index=False)







