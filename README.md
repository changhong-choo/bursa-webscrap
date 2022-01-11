# Bursa Malaysia WebScrap
Simple program to extract data from Bursa Malaysia website using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Selenium](https://www.selenium.dev/) in [Python](https://www.python.org/). The data extracted is then presented in [Power BI](https://powerbi.microsoft.com/en-us/).

## Description
The program is able to extract equities and indices daily movements in [Bursa Malaysia](https://www.bursamalaysia.com/) and save the data in a csv file. As the project is mainly for practise purpose, the equities information extracted is only from the [Main Market](https://www.bursamalaysia.com/market_information/equities_prices?keyword=&top_stock=top_active&board=MAIN-MKT&alphabetical=&sector=&sub_sector=). 

## Getting started
1. Run both the .py file and the data will be stored in separate csv files in your working directory.
2. Open bursaPowerBI.pbix file and change the data source location
3. Refresh data in Power BI.
4. Done!

![Screenshot](https://github.com/changhong-choo/bursa-webscrap/blob/main/power-bi/powerbi.PNG)

# Further improvement
1. Integrate both programs into one
2. Automate the daily program
