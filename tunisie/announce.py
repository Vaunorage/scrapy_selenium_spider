import json
import re
import time
from playwright.sync_api import sync_playwright
from subprocess import call
from scrapy import Selector
import schedule


def get(Country='Tunisie', Gouvernorat='', Delegation='', Localite='', Rubrique='', Nature='', Type='', Code='',
        with_photos=None, price_min='', price_max='', surface_min='', surface_max='', pro='Indifferent', save=None,
        recurrence=None, headless=None):
    if recurrence:
        # will run every hour
        # recurrence = 60 minutes => 1 hour
        schedule.every(recurrence).minutes.do(scrap_job, Country, Gouvernorat, Delegation, Localite, Rubrique, Nature, Type, Code,
        with_photos, price_min, price_max, surface_min, surface_max, pro, save, headless)
        while True:
            print("\r [+] Waiting..",end='')
            schedule.run_pending()
            time.sleep(1)
    else:
        scrap_job(Country, Gouvernorat, Delegation, Localite, Rubrique, Nature, Type, Code,
        with_photos, price_min, price_max, surface_min, surface_max, pro, save, headless)



def scrap_job(Country, Gouvernorat, Delegation, Localite, Rubrique, Nature, Type, Code,
        with_photos, price_min, price_max, surface_min, surface_max, pro, save, headless):
    play = sync_playwright().start()
    print('\n [+] Browser started')
    browser = play.firefox.launch(headless=headless)

    page = browser.new_page()
    page.goto('http://www.tunisie-annonce.com/AnnoncesImmobilier.asp')
    print(' [+] Setting inputs')
    page.locator("//div[@id='combo_pay']").click()
    page.locator("//div[@style='width: 100%; overflow: hidden;']", has_text=Country).click()
    time.sleep(1)
    if Gouvernorat:
        page.locator("//div[@id='combo_reg']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']", has_text=Gouvernorat).click()
        time.sleep(1)
    if Delegation:
        page.locator("//div[@id='combo_vil']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']", has_text=Delegation).click()
        time.sleep(1)
    if Localite:
        page.locator("//div[@id='combo_loc']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']", has_text=Localite).click()
        time.sleep(1)
    if Rubrique:
        page.locator("//div[@id='combo_rub']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']", has_text=Rubrique).click()
        time.sleep(1)
    if Nature:
        page.locator("//div[@id='combo_typ']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']", has_text=Nature).first.click()
        time.sleep(1)
    if Type:
        page.locator("//div[@id='combo_sou_typ']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']", has_text=Type).click()
        time.sleep(1)
    if Code:
        page.fill("//input[@id='rech_cod_ann']", str(Code))
        time.sleep(1)
    if with_photos:
        page.check("//input[@id='rech_photo']")
        time.sleep(1)
    if price_min:
        page.fill("//input[@id='rech_prix_min']", str(price_min))
        time.sleep(1)
    if price_max:
        page.fill("//input[@id='rech_prix_max']", str(price_max))
        time.sleep(1)
    if surface_min:
        page.fill("//input[@id='rech_surf_min']", str(surface_min))
        time.sleep(1)
    if surface_max:
        page.fill("//input[@id='rech_surf_max']", str(surface_max))
        time.sleep(1)
    if pro == 'Indifferent':
        pass
    elif pro == 'Particulier':
        page.select_option("//select[@id='rech_typ_cli']", value='1')
    elif pro == 'Professionnel':
        page.select_option("//select[@id='rech_typ_cli']", value='2')
    page.locator("//li[@class='search']/a").click()
    time.sleep(5)
    source = page.content()
    play.stop()
    print(' [+] Browser closed')
    sel = Selector(text=source)
    results = sel.xpath("//table[@class='RecordsNumber']//td/b[1]/text()").get()
    matched = re.search(".*[0-9]", results).group()
    total_records = int(matched.replace(" ", ''))
    print(f' [+] Records = {total_records}')
    if not total_records == 0:
        with open("config.json", 'w') as f:
            json.dump({'source': source}, f)
        print(" [+] Starting Crawling")
        filename = Country + "_" + Gouvernorat
        call(['scrapy', 'crawl', 'tunisie_spider', '-a', f'save={save}', '-o', f'{filename}.csv'])
        print(" [+] Finished")
        print(f" [+] Generated file {filename}.csv")
    else:
        print(" [+] No records found ")
