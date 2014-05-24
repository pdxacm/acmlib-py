DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
DATE_FORMAT = '%Y-%m-%d'

DEFAULT_BASE_URL = "http://www.acm.pdx.edu"
    
import datetime

def format_date(d):
    return datetime.datetime.strftime(d, DATE_FORMAT)

def format_datetime(d):
    return datetime.datetime.strftime(d, DATETIME_FORMAT)

from .main import AcmLib
