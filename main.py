import ctypes
import datetime as dt
import random
import smtplib

ctypes.windll.shell32.IsUserAnAdmin()
my_email = "deepak.kumar2305@gmail.com"
password = "zgvkrwjgikynbwyw"
receiver = "deepak.ram@infocepts.com"
cc = "nightrider.180@gmail.com"
bcc = "er.deepak.kumar2305@gmail.com"
message_subject = "Subject:Motivational Quote for You."
now = dt.datetime.now()
week_day = now.weekday()
if week_day == 6:
    with open("quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()
        email_body = random.choice(quotes_list)
    message = "From: %s\r\n" % my_email + "To: %s\r\n" % receiver + "CC: %s\r\n" % cc + "Subject: %s\r\n" % message_subject + "\r\n" + email_body + "\nBTW I've sent this email from my Python code!"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(my_email, receiver, message)
