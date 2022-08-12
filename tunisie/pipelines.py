# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter
from rich.pretty import pprint


class TunisiePipeline:
    def process_item(self, item, spider):
        return item
        
class SQLite_Pipeline:
    def __init__(self):
        self.count = 0
        # change the database name accordingly
        self.con = sqlite3.connect("announce.db")
        self.cur = self.con.cursor()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS listings(
                ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                Reference TEXT,
                Title TEXT,
                Category TEXT,
                Localisation TEXT,
                Adresse TEXT,
                Prix TEXT,
                Texte TEXT,
                Inseree TEXT,
                Modifiee TEXT
            )
            """,
        )
    
    def process_item(self,item,spider):
        # if bool(item['Save']):
        if spider.save_db:
            self.cur.execute("""SELECT * FROM listings WHERE Reference = ? AND Prix = ? """,(item['Reference'],item['Prix']))
            exist = self.cur.fetchone()
            if exist:
                self.count +=1
                # spider.logger.warn("[+] Item already exist in the database\n")
                print(f" [+] Item already exist in the database {self.count}\n")
                return item
            else:
                self.count +=1
                print(f"\r [+] ITEM added to DB {self.count}",end='')
                self.cur.execute(
                    """
                    INSERT INTO listings(Reference,Title,Category,Localisation,Adresse,Prix,Texte,Inseree,Modifiee) VALUES (?,?,?,?,?,?,?,?,?)
                    """,
                    (
                    item['Reference'],
                    item['Title'],
                    item['Category'],
                    item['Localisation'],
                    item['Adresse'],
                    item['Prix'],
                    item['Texte'],
                    item['Inseree'],
                    item['Modifiee'],
                    )
                )
                self.con.commit()
                return item
        else:
            print(f"\r [+] ITEM Processed {self.count}",end='')
            return item
