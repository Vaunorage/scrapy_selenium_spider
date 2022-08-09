from selenium import webdriver
from scrapy.selector import Selector
import re
from urllib.parse import urljoin
import json
from subprocess import Popen,call

def driver():
    url = 'http://www.tunisie-annonce.com/AnnoncesImmobilier.asp'
    driver = webdriver.Firefox(executable_path="/home/lubuntu/scrapy_projects/tunisie/tunisie/geckodriver")
    driver.get(url)
    input("Press 1 to continue : ")
    source = driver.page_source
    sel = Selector(text=source)
    results = sel.xpath("//table[@class='RecordsNumber']//td/b[1]/text()").get()
    matched = re.search(".*[0-9]",results).group()
    total_records = int(matched.replace(" ",''))
    if total_records > 25:
        next_page = sel.xpath("//td[@width='40'][3]/a/@href").get()
        next_page = urljoin(url,next_page)
    else:
        next_page = None
    config = {"source":source,"next":next_page,"records":total_records}
    with open("config.json","w") as f:
        json.dump(config,f)
    # print("\nResult: ",total_records,next_page)
    driver.close()

driver()
call(['scrapy', 'crawl','tunisie_spider'])