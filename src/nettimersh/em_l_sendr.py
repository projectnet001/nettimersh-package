import smtplib
print("Be informed that gmail blocks less secure apps access to your gmail account")
print("Therefore here we use microosft outlook accounts")
sender = input("Enter your email address: ")
password = input("Enter your password: ")
recipient = input("Enter the recipient's email address: ")
content = input("Enter the message you want to send: ")
mail=smtplib.SMTP('smtp.office365.com',587)
mail.starttls()
mail.login(sender,password)
mail.ehlo()
header='To:'+recipient+'\n'+'From:'+sender+'\n'+'Subject:testmail\n\n'
message=header+content
mail.sendmail(sender,recipient, message)
mail.close()