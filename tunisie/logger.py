# import logging
import datetime
# logging.basicConfig(format='[%(asctime)s] - %(message)s')

# my_logger = logging.getLogger('mylogger')
# my_logger.setLevel(logging.INFO)


class my_logger:
    @staticmethod
    def info(message):
        print(f"INFO: [{datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}] {message}")

    @staticmethod
    def warn(message):
        print(f"WARN: [{datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}] {message}")


# print([k for k in logging.Logger.manager.loggerDict])
#
# for k, v in logging.Logger.manager.loggerDict.items():
#     if 'scrapy' in k:
#         v.disabled = True
