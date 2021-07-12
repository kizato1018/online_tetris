import logging
import datetime
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s [%(levelname)s]  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

log_folder = f'{os.path.dirname(os.path.abspath(__file__))}/logs/'
os.makedirs(log_folder, exist_ok=True)
log_filename = f'{log_folder}{datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")}'
fh = logging.FileHandler(log_filename)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)
