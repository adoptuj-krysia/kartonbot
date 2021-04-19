from random import randrange
from datetime import time
from kartonbot_py.common.date_utils import is_date_easter_sunday

mapper_rules = [
    {
        "msg_group": "messages_special",
        "img_group": "special",
        "applicable": lambda today_date: randrange(1, 1001) == 1000
    },

    {
        "msg_group": "messages_420",
        "img_group": "420",
        "applicable": lambda today_date: time(4, 19) < today_date.time() < time(4, 25)
    },

    {
        "msg_group": "messages_2137",
        "img_group": "papa",
        "applicable": lambda today_date: (today_date.hour, today_date.minute) == (21, 37),
    },

    {
        "msg_group": "messages_halloween",
        "img_group": "halloween",
        "applicable": lambda today_date: (today_date.day, today_date.month) == (31, 10)
    },

    {
        "msg_group": "messages_6th_december",
        "img_group": "santa",
        "applicable": lambda today_date: (today_date.day, today_date.month) == (6, 12)
    },

    {
        "msg_group": "messages_christmas",
        "img_group": "santa",
        "applicable": lambda today_date: 24 <= today_date.day <= 26 and today_date.month == 12
    },

    {
        "msg_group": "messages_easter",
        "img_group": "easter",
        "applicable": lambda today_date: is_date_easter_sunday(today_date)
    },

    {
        "msg_group": "messages_fathers_day",
        "img_group": "father",
        "applicable": lambda today_date: (today_date.day, today_date.month) == (23, 6)
    },

    {
        "msg_group": "messages_mothers_day",
        "img_group": "mother",
        "applicable": lambda today_date: (today_date.day, today_date.month) == (26, 5)
    },

    {
        "msg_group": "messages_childrens_day",
        "img_group": "children",
        "applicable": lambda today_date: (today_date.day, today_date.month) == (1, 6)
    },

    {
        "msg_group": "messages_new_years_eve",
        "img_group": "party",
        "applicable": lambda today_date: (today_date.day, today_date.month) == (31, 12)
    },

    {
        "msg_group": "messages_new_year",
        "img_group": "party",
        "applicable": lambda today_date: (today_date.day, today_date.month) == (1, 1)
    },

    {
        "msg_group": "messages_polish_patriot",
        "img_group": "poland",
        "applicable": lambda today_date: (today_date.day, today_date.month) in [(11, 11), (1, 5), (3, 5), (1, 8)]
    },

    {
        "msg_group": "messages_morning",
        "img_group":  "morning",
        "applicable": lambda today_date: today_date.time().hour in range(6, 13)
    },

    {
        "msg_group": "messages_noon",
        "img_group": "noon",
        "applicable": lambda today_date: today_date.time().hour in range(13, 18)
    },

    {
        "msg_group": "messages_evening",
        "img_group": "evening",
        "applicable": lambda today_date: today_date.time().hour in range(18, 23)
    },

    {
        "msg_group": "messages_night",
        "img_group": "night",
        "applicable": lambda today_date: today_date.time().hour == 23 or today_date.time().hour in range(0, 6)
    }
]

