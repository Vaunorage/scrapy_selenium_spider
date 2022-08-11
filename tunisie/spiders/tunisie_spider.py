import json
import re
from threading import local
from tkinter.tix import Select
from urllib.parse import parse_qs, urlparse
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from ..items import TunisieItem
from scrapy.loader import ItemLoader
from rich.console import Console

class TunisieSpiderSpider(scrapy.Spider):
    name = 'tunisie_spider'
    allowed_domains = ['tunisie-annonce.com']
    count = 0
    con = Console()

    def start_requests(self):
        url = 'http://www.tunisie-annonce.com'
        yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        # change path according to your system
        with open("spiders/config.json",'r') as f:
            config = json.load(f)
        resp= config.get("source")
        next_page = config.get("next")
        records = config.get("records")
        sel = Selector(text=resp)
        for row in sel.xpath("//tr[@class='Tableau1']"):
            self.count +=1
            listing_url = response.urljoin(row.xpath("./td[8]/a/@href").get())
            yield scrapy.Request(url=listing_url,callback=self.parse_listing)
            # loader = ItemLoader(item=TunisieItem())
            # region = row.xpath("./td[2]/a/text()").get()
            # nature = row.xpath("./td[4]/text()").get()
            # typpe = row.xpath("./td[6]/text()").get()
            # annonce = row.xpath("./td[8]/a/text()").get()
            # prix = row.xpath("./td[10]/text()").get()
            # modifiee = row.xpath("./td[12]/text()").get()

            # loader.add_value("Region",value=region)
            # loader.add_value("Nature",value=nature)
            # loader.add_value("Type",value=typpe)
            # loader.add_value("Annonce",value=annonce)
            # loader.add_value("Prix",value=prix)
            # loader.add_value("Modifiee",value=modifiee)

            # yield loader.load_item()
        if next_page:
            url = next_page
            yield scrapy.Request(url,callback=self.parse_pagination,cb_kwargs={"next_page":url,"records":records})
    
    def parse_pagination(self,response,next_page,records):
        sel = Selector(text=response.text)
        for row in sel.xpath("//tr[@class='Tableau1']"):
            self.count +=1
            listing_url = response.urljoin(row.xpath("./td[8]/a/@href").get())
            yield scrapy.Request(url=listing_url,callback=self.parse_listing)
            # loader = ItemLoader(item=TunisieItem())
            # region = row.xpath("./td[2]/a/text()").get()
            # nature = row.xpath("./td[4]/text()").get()
            # typpe = row.xpath("./td[6]/text()").get()
            # annonce = row.xpath("./td[8]/a/text()").get()
            # prix = row.xpath("./td[10]/text()").get()
            # modifiee = row.xpath("./td[12]/text()").get()

            # loader.add_value("Region",value=region)
            # loader.add_value("Nature",value=nature)
            # loader.add_value("Type",value=typpe)
            # loader.add_value("Annonce",value=annonce)
            # loader.add_value("Prix",value=prix)
            # loader.add_value("Modifiee",value=modifiee)

            # yield loader.load_item()
        while True:
            try:
                q = urlparse(next_page)
                q_dict = parse_qs(q.query)
                page = q_dict.get("rech_page_num")[0]
                if self.count < records:
                    url = next_page.replace(f"rech_page_num={page}",f"rech_page_num={int(page)+1}")
                    yield scrapy.Request(url,callback=self.parse_pagination,cb_kwargs={"next_page":url,"records":records})
                else:
                    break
            except Exception as e:
                self.con.print_exception()
                break
            else:
                continue
                
    def parse_listing(self,response):
        reference,title,category,localization,adresse,prix,texte,inseree,modifiee,tel,mob,main = 'None','None','None','None','None','None','None','None','None','None','None','None'
        sel = Selector(text=response.text)
        loader = ItemLoader(item=TunisieItem())
        try:
            for row in sel.xpath("//table[@class='da_rub_cadre'][2]//table[@align='center']//tr"):
                flag = row.xpath("./td/text()").get()
                if flag:
                    try:
                        f = row.xpath("./td[@colspan='6']")
                        if row.xpath("./td[@colspan='6']"):
                            raw_ref = row.xpath("./td[@colspan='6']/text()").get()
                            try:
                                ref = re.search("(?:\[)(.*)(?:\])",raw_ref).group()
                                reference = "".join([l for l in ref if l.isdigit()])
                            except:
                                pass
                            try:
                                title = re.search("\s[A-Z a-z].*",raw_ref).group().strip()
                            except:
                                pass
                        else:
                            name = row.xpath("./td[1]//text()").get()
                            if "cat" in name.lower():
                                try:
                                    category = "".join(row.xpath("./td[2]//text()").getall())
                                except:
                                    pass
                            elif "local" in name.lower():
                                try:
                                    localization = "".join(row.xpath("./td[2]//text()").getall())
                                except:
                                    pass
                            elif "adresse" in name.lower():
                                try:
                                    adresse = "".join(row.xpath("./td[2]//text()").getall())
                                except:
                                    pass
                            elif "prix" in name.lower():
                                try:
                                    prix = "".join(row.xpath("./td[2]//text()").getall())
                                    prix = re.search(".*[0-9]\s",prix).group()
                                except:
                                    pass
                            elif "texte" in name.lower():
                                try:
                                    texte = "".join(row.xpath("./td[2]//text()").getall())
                                except:
                                    pass
                            elif "Insérée".lower() in name.lower(): 
                                try:
                                    inseree = "".join(row.xpath("./td[2]//text()").getall())
                                except:
                                    pass
                                try:
                                    modifiee = "".join(row.xpath("./td[4]//text()").getall())
                                except:
                                    pass
                    except Exception as e:
                        self.con.print("Error in parsing")
                        print(e)
                    
            try:
                tel = sel.xpath("//table[@class='da_rub_cadre_contact']//li[@class='phone']/span/text()").get()
            except:
                pass
            try:
                mob = sel.xpath("//table[@class='da_rub_cadre_contact']//li[@class='cellphone']/span/text()").get()
            except:
                pass
            try:
                mail = sel.xpath("//table[@class='da_rub_cadre_contact']//li[@class='fax']/span/text()").get()
            except:
                pass
            loader.add_value("Reference",value=reference)
            loader.add_value("Title",value=title)
            loader.add_value("Category",value=category)
            loader.add_value("Localisation",value=localization)
            loader.add_value("Adresse",value=adresse)
            loader.add_value("Prix",value=prix)
            loader.add_value("Texte",value=texte)
            loader.add_value("Inseree",value=inseree)
            loader.add_value("Modifiee",value=modifiee)
            # self.con.print(reference,title,category,localization,adresse,prix,texte,inseree,modifiee,tel,mob,main)
            yield loader.load_item()
        except Exception as e:
            print(e)
            self.con.print("error in main")
