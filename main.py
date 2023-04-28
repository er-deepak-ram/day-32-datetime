import datetime as dt
import random

now = dt.datetime.now()
week_day = now.weekday()
if week_day == 3:
    with open("quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()
        email_body = random.choice(quotes_list)
