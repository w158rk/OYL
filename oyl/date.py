import datetime

def string_to_date(s):
    return datetime.datetime.strptime(s, "%Y-%m-%d")

def date_to_string(d):
    return datetime.datetime.strftime(d, "%Y-%m-%d")
