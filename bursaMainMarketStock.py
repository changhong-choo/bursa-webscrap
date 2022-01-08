from bs4 import BeautifulSoup as bs
from datetime import datetime
import requests
import pandas as pd

# Set the url and headers for connection purpose
url = 'https://www.bursamalaysia.com/market_information/equities_prices?keyword=&top_stock=top_active&board=MAIN-MKT&alphabetical=&sector=&sub_sector=&page='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
dfs = []
max_page = 51

# Get the stocks information
for page in range(1, max_page):
    
    r = requests.get(url + str(page), headers=headers)
    
    soup = bs(r.text, 'html.parser')
    table = soup.find('div', {'class' : 'mb-2'})
    a = table.find('table', {'class' : 'table datatable-striped text-center equity_prices_table datatable-with-sneak-peek js-anchor-price-table d-none d-lg-block'})
    df = pd.read_html(str(a))[0]
    dfs.append(df)
    
b = pd.concat(dfs)


# Export data to csv
filename = datetime.now().strftime('bursaMainMarketStock_%Y%m%d.csv')
b.to_csv(filename, index=False)
