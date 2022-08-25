# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#
#
# # useful for handling different item types with a single interface
# import sqlite3
# from itemadapter import ItemAdapter
# from rich.pretty import pprint
#
#
# class TunisiePipeline:
#     def process_item(self, item, spider):
#         return item
#
# class SQLite_Pipeline:
#     def __init__(self):
#         self.count = 0
#         # change the database name accordingly
#         self.con = sqlite3.connect("announce.db")
#         self.cur = self.con.cursor()
#         self.cur.execute(
#             """
#             CREATE TABLE IF NOT EXISTS listings(
#                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                 Reference TEXT,
#                 Title TEXT,
#                 Category TEXT,
#                 Localisation TEXT,
#                 Adresse TEXT,
#                 Prix TEXT,
#                 Texte TEXT,
#                 Inseree TEXT,
#                 Modifiee TEXT,
#                 Telephone TEXT,
#                 Mobile TEXT,
#                 Fax TEXT,
#                 Images TEXT
#             )
#             """,
#         )
#
#     def process_item(self,item,spider):
#         # if bool(item['Save']):
#         if spider.save_db:
#             self.cur.execute("""SELECT * FROM listings WHERE Reference = ? AND Prix = ? """,(item['Reference'],item['Prix']))
#             exist = self.cur.fetchone()
#             if exist:
#                 self.count +=1
#                 # spider.logger.warn("[+] Item already exist in the database\n")
#                 print(f" [+] Item already exist in the database {self.count}\n")
#                 print(spider.save_db)
#                 return item
#             else:
#                 self.count +=1
#                 print(f"\r [+] ITEM added to DB {self.count}",end='')
#                 self.cur.execute(
#                     """
#                     INSERT INTO listings(Reference,Title,Category,Localisation,Adresse,Prix,Texte,Inseree,Modifiee,Telephone,Mobile,Fax,Images) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
#                     """,
#                     (
#                     item['Reference'],
#                     item['Title'],
#                     item['Category'],
#                     item['Localisation'],
#                     item['Adresse'],
#                     item['Prix'],
#                     item['Texte'],
#                     item['Inseree'],
#                     item['Modifiee'],
#                     item['Telephone'],
#                     item['Mobile'],
#                     item['Fax'],
#                     item['Images']
#                     )
#                 )
#                 self.con.commit()
#                 return item
#         else:
#             self.count +=1
#             print(f"\r [+] ITEM Processed {self.count}",end='')
#             return item

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from datetime import datetime

import pandas as pd
from sqlalchemy import inspect


class TunisiePipeline:
    def process_item(self, item, spider):
        return item


class SQLite_Pipeline:

    def open_spider(self, spider):
        self.count = 0
        # change the database name accordingly
        self.con = sqlite3.connect("announce.db")

    def close_spider(self, spider):
        self.con.close()

    def process_item(self, item, spider):
        if spider.save_db:

            try:
                # creates the dataframe

                item_dict = dict(item)
                tmp_df = pd.DataFrame({e: [item_dict[e]] for e in item_dict})
                tmp_df['Updated'] = datetime.now()

                # creates the table if not exists
                tmp_df.head(0).to_sql(name='listings', con=self.con, if_exists='append')

                # checks if item exists
                exists = pd.read_sql(f"select * from listings where Reference={item['Reference']}"
                                     f" AND Modifiee='{item['Modifiee']}'", con=self.con)

                text_item = f"\r [+] Processing : COUNT : {self.count}, REFERENCE : {item['Reference']}," \
                            f" MODIFIEE : {item['Modifiee']}"

                if exists.empty:

                    tmp_df.to_sql(name='listings', con=self.con, if_exists='append')

                    print(text_item + " ITEM added to DB", end='')
                else:

                    print(text_item + " ITEM found not added to DB", end='')

                self.count += 1

                return item
            except Exception as e:
                print(f"Exception : {e}")
                return item
        else:
            self.count += 1
            print(f"\r [+] ITEM Processed {self.count}", end='')
            return item