import logging

logging.basicConfig(format='[%(asctime)s] - %(message)s')

my_logger = logging.getLogger('mylogger')
my_logger.setLevel(logging.INFO)

for k, v in logging.Logger.manager.loggerDict.items():
    if 'mylogger' not in k:
        v.disabled = True