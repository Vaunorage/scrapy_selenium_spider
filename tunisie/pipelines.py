# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from datetime import datetime

import pandas as pd
from sqlalchemy import inspect

from tunisie.logger import my_logger

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
        if spider.save:

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

                text_item = f"\r [+] Processing : COUNT : {self.count}/{spider.total_nb}, REFERENCE : {item['Reference']}," \
                            f" MODIFIEE : {item['Modifiee']}"

                if exists.empty:

                    tmp_df.to_sql(name='listings', con=self.con, if_exists='append')

                    my_logger.info(text_item + " ITEM added to DB", end='')
                else:

                    my_logger.info(text_item + " ITEM found not added to DB", end='')

                self.count += 1

                return item
            except Exception as e:
                my_logger.warn(f"Exception : {e}")
                return item
        else:
            self.count += 1
            my_logger.info(f" ITEM Processed {self.count}", end='')
            return item
