import datetime


def current_utc_timestamp():
    return datetime.datetime.now().strftime("%s")
