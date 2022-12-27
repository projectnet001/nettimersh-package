#!/usr/bin/python3

import smtplib

sender = 'sender@fromdomain.com'
receivers = ['receiver@todomain.com']

message = """From: From Person <sender@fromdomain.com>
To: To Person <receiver@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost',55678)
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except Exception:
   print("Error: unable to send email")