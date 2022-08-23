# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from datetime import datetime

import scrapy
from itemloaders.processors import MapCompose, TakeFirst


def clean(value):
    value = value.replace("\xa0\xa0", '')
    value = value.replace("\xa0", '')
    return value


def handle_prix(val):
    val = val.replace("\xa0\xa0", '')
    val = val.replace("\xa0", '')
    val = val.replace(' ', '')
    return val


class TunisieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Reference = scrapy.Field(
        input_processor=MapCompose(clean, str.strip),
        output_processor=TakeFirst()
    )
    Title = scrapy.Field(
        input_processor=MapCompose(clean, str.strip),
        output_processor=TakeFirst()
    )
    Category = scrapy.Field(
        input_processor=MapCompose(clean, str.strip),
        output_processor=TakeFirst()
    )
    Localisation = scrapy.Field(
        input_processor=MapCompose(clean, str.strip),
        output_processor=TakeFirst()
    )
    Adresse = scrapy.Field(
        input_processor=MapCompose(clean, str.strip),
        output_processor=TakeFirst()
    )
    Prix = scrapy.Field(
        input_processor=MapCompose(handle_prix, str.strip),
        output_processor=TakeFirst()
    )
    Texte = scrapy.Field(
        input_processor=MapCompose(clean, str.strip),
        output_processor=TakeFirst()
    )
    Inseree = scrapy.Field(
        input_processor=MapCompose(clean, str.strip),
        output_processor=TakeFirst()
    )
    Modifiee = scrapy.Field(
        input_processor=MapCompose(clean, str.strip),
        output_processor=TakeFirst()
    )
    Telephone = scrapy.Field(
        input_processor=MapCompose(clean, str.strip),
        output_processor=TakeFirst()
    )
    Mobile = scrapy.Field(
        input_processor=MapCompose(clean, str.strip),
        output_processor=TakeFirst()
    )
    Fax = scrapy.Field(
        input_processor=MapCompose(clean, str.strip),
        output_processor=TakeFirst()
    )
    Images = scrapy.Field(
        input_processor=MapCompose(clean, str.strip),
        output_processor=TakeFirst()
    )
