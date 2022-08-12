# import requests


# r = requests.get("https://httpbin.org/ip",proxies={"https":"http://DAC1mbvX26j8AcDQ:wifi;us;;;;@resi3.ipb.cloud:9000"},timeout=4)
# print(r.text)

import json
import re
import time
from playwright.sync_api import sync_playwright
from subprocess import call
from rich.pretty import pprint
from scrapy import Selector
import schedule

def get(Country='Tunisie',Gouvernorat='',Delegation='',Localite='',Rubrique='',Nature='',Type='',Code='',with_photos=False,price_min='',price_max='',surface_min='',surface_max='',pro='Indifferent',save=True,recurrence=None,headless=True):
    schedule.every().day.at('12:52').do(driver,Country='Tunisie',Gouvernorat='',Delegation='',Localite='',Rubrique='',Nature='',Type='',Code='',with_photos=False,price_min='',price_max='',surface_min='',surface_max='',pro='Indifferent',save=True,recurrence=None,headless=True)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
def driver(Country='Tunisie',Gouvernorat='',Delegation='',Localite='',Rubrique='',Nature='',Type='',Code='',with_photos=False,price_min='',price_max='',surface_min='',surface_max='',pro='Indifferent',save=True,recurrence=None,headless=True):
    play = sync_playwright().start()
    # pprint({
    #     'Inputs':{
    #         'Country':Country,
    #         'Gouvernorat':Gouvernorat,
    #         'Delegation':Delegation,
    #         'Localite':Localite,
    #         'Rubrique':Rubrique,
    #         'Nature':Nature,
    #         'Type':Type,
    #         'Code':Code,
    #         'with_photos':with_photos,
    #         'price_min':price_min,
    #         'price_max':price_max,
    #         'surface_min':surface_min,
    #         'surface_max':surface_max,
    #         'pro':pro,
    #         'save':save,
    #         'recurrence':recurrence
    #     }
    # },expand_all=True)
    print(' [+] Browser started')
    if headless:
        browser = play.chromium.launch(headless=True)
    else:
        browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('http://www.tunisie-annonce.com/AnnoncesImmobilier.asp')
    print(' [+] Setting inputs')
    page.locator("//div[@id='combo_pay']").click()
    page.locator("//div[@style='width: 100%; overflow: hidden;']",has_text=Country).click()
    time.sleep(1)
    if Gouvernorat:
        page.locator("//div[@id='combo_reg']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']",has_text=Gouvernorat).click()
        time.sleep(1)
    if Delegation:
        page.locator("//div[@id='combo_vil']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']",has_text=Delegation).click()
        time.sleep(1)
    if Localite:
        page.locator("//div[@id='combo_loc']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']",has_text=Localite).click()
        time.sleep(1)
    if Rubrique:
        page.locator("//div[@id='combo_rub']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']",has_text=Rubrique).click()
        time.sleep(1)
    if Nature:
        page.locator("//div[@id='combo_typ']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']",has_text=Nature).first.click()
        time.sleep(1)
    if Type:
        page.locator("//div[@id='combo_sou_typ']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']",has_text=Type).click()
        time.sleep(1)
    if Code:
        page.fill("//input[@id='rech_cod_ann']",str(Code))
        time.sleep(1)
    if with_photos:
        page.check("//input[@id='rech_photo']")
        time.sleep(1)
    if price_min:
        page.fill("//input[@id='rech_prix_min']",str(price_min))
        time.sleep(1)
    if price_max:
        page.fill("//input[@id='rech_prix_max']",str(price_max))
        time.sleep(1)
    if surface_min:
        page.fill("//input[@id='rech_surf_min']",str(surface_min))
        time.sleep(1)
    if surface_max:
        page.fill("//input[@id='rech_surf_max']",str(surface_max))
        time.sleep(1)
    if pro == 'Indifferent':
        pass
    elif pro == 'Particulier':
        page.select_option("//select[@id='rech_typ_cli']",value='1')
    elif pro == 'Professionnel':
        page.select_option("//select[@id='rech_typ_cli']",value='2')
    page.locator("//li[@class='search']/a").click()
    time.sleep(5)
    source = page.content()
    play.stop()
    print(' [+] Browser closed')
    sel = Selector(text=source)
    results = sel.xpath("//table[@class='RecordsNumber']//td/b[1]/text()").get()
    matched = re.search(".*[0-9]",results).group()
    total_records = int(matched.replace(" ",''))
    if not total_records == 0:
        with open("config.json",'w') as f:
            json.dump({'source':source},f)
        print(" [+] Starting Crawling")
        filename = Country+"_"+Gouvernorat
        call(['scrapy','crawl','tunisie_spider','-a',f'save={save}','-o',f'{filename}.csv'])
        print(" [+] Finished")
        print(f" [+] Generated file {filename}.csv")
    else:
        print(" [+] No records found ")
    