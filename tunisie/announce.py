import json
import re
import time

from playwright.sync_api import sync_playwright
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from spiders.tunisie_spider import TunisieSpider
from scrapy import Selector
import schedule

from tunisie.logger import my_logger


def get(country, gouvernerat='', delegation='', localite='', rubrique='', nature='',
        type='', code='', with_photos=None, price_min='', price_max='', surface_min='', surface_max='',
        pro='Indifferent', sort=None, save=True, recurrence=None, headless=True):
    if recurrence:
        schedule.every(recurrence).minutes.do(scrap_job, country, gouvernerat, delegation, localite, rubrique, nature,
                                              type, code, with_photos, price_min, price_max, surface_min, surface_max,
                                              pro, sort, save, headless)
        while True:
            print("\r [+] Waiting..", end='')
            schedule.run_pending()
            time.sleep(1)
    else:
        scrap_job(country, gouvernerat, delegation, localite, rubrique, nature, type, code, with_photos, price_min,
                  price_max, surface_min, surface_max, pro, sort, save, headless)


def scrap_job(country, gouvernorat, delegation, localite, rubrique, nature, type, code, with_photos, price_min,
              price_max, surface_min, surface_max, pro, sort, save, headless):
    play = sync_playwright().start()
    my_logger.info('Browser started')
    browser = play.firefox.launch(headless=headless)

    page = browser.new_page()
    page.goto('http://www.tunisie-annonce.com/AnnoncesImmobilier.asp')
    my_logger.info('Setting inputs')
    page.locator("//div[@id='combo_pay']").click()
    page.locator("//div[@style='width: 100%; overflow: hidden;']", has_text=country).click()
    time.sleep(1)

    if gouvernorat:
        page.locator("//div[@id='combo_reg']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']", has_text=gouvernorat).click()
        time.sleep(1)

    if delegation:
        page.locator("//div[@id='combo_vil']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']", has_text=delegation).click()
        time.sleep(1)

    if localite:
        page.locator("//div[@id='combo_loc']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']", has_text=localite).click()
        time.sleep(1)

    if rubrique:
        page.locator("//div[@id='combo_rub']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']", has_text=rubrique).click()
        time.sleep(1)

    if nature:
        page.locator("//div[@id='combo_typ']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']", has_text=nature).first.click()
        time.sleep(1)

    if type:
        page.locator("//div[@id='combo_sou_typ']").click()
        page.locator("//div[@style='width: 100%; overflow: hidden;']", has_text=type).click()
        time.sleep(1)

    #TODO : fix
    # if sort:
    #     page.locator("//*[@id='rech_order_by']").click()
    #     page.locator("//*[@style='width: 100%; overflow: hidden;']", has_text=sort).click()
    #     time.sleep(1)

    if code:
        page.fill("//input[@id='rech_cod_ann']", str(code))
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
    my_logger.info('Browser closed')
    sel = Selector(text=source)
    results = sel.xpath("//table[@class='RecordsNumber']//td/b[1]/text()").get()
    matched = re.search(".*[0-9]", results).group()
    total_records = int(matched.replace(" ", ''))
    if not total_records == 0:
        with open("config.json", 'w') as f:
            json.dump({'source': source}, f)
        my_logger.info("Starting Crawling")

        settings = get_project_settings()
        process = CrawlerProcess(settings=settings)
        process.crawl(TunisieSpider, save=save)
        process.start()
        my_logger.info("Finished")
    else:
        my_logger.info("No records found ")
