#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
Send mail to a .csv list of users, with contents from message.txt
"""

import csv
import time
import smtplib
from email.mime.text import MIMEText
sender = 'techsysday@gmail.com'
message = open('body.txt').read()
message = MIMEText(s.encode('utf-8'), 'plain', 'utf-8')
print("Connecting to gmail...")
session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.ehlo
print("Authenticating...")
session.login(sender, open('from.txt').readline())


print("Parsing recipient list...")
recipient_list = []
with open('to.txt') as tofile:
    for row in tofile:
        recipient_list.append(row)
print("Sending mail to %s recipients." % (len(recipient_list)))

for recipient_email in recipient_list:
    print("\t %s" % (recipient_email))
    headers = ["From: Python Viet Nam <" + sender + ">",
               "Subject: " + "Thong bao",
               "To: " + recipient_email,
               "MIME-Version: 1.0",
               "Content-Type: text/html;charset=utf-8"]
    headers = "\r\n".join(headers)
    session.sendmail(sender, recipient_email, headers + "\r\n\r\n" + message)
    time.sleep(5)

print("All done!")
