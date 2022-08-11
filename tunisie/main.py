from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from scrapy.selector import Selector
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import re
from urllib.parse import urljoin
import json
from subprocess import Popen,call
from webdriver_manager.firefox import GeckoDriverManager


# no need to specify headless mode, because in our case we always need headed mode.
def init_driver():
    # will automatically install latest webdriver first time then will reuse the cache
    # no need to specify executable path
    service = Service(GeckoDriverManager().install()) 
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", user_agent)
    driver = webdriver.Firefox(service=service)
    return driver

def start_driver():
    url = 'http://www.tunisie-annonce.com/AnnoncesImmobilier.asp'
    driver = init_driver()
    driver.maximize_window()
    # change path according to your system
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
    with open("spiders/config.json","w") as f:
        json.dump(config,f)
    driver.close()

start_driver()
call(['scrapy', 'crawl','tunisie_spider'])