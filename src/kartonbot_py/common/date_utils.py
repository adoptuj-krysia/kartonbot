from datetime import datetime
_default_formatter = "%d.%m.%Y, %H:%M:%S"


def date_to_str(date):
    return date.strftime(_default_formatter)


def str_to_date(string):
    return datetime.strptime(string, _default_formatter)


def is_date_easter_sunday(date):
    year = date.year

    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7

    month = (h - m + r + 90) // 25
    day = (h - m + r + month + 19) % 32

    return month == date.month and day == date.day
