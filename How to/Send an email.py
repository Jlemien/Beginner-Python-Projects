import smtplib
import imapclient
import pyzmail
import APScheduler

to = 'joseph.lemien@vericant.com'
gmail_user = 'joseph.lemien@gmail.com'
gmail_pwd = 'banananutmuffins'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
msg = header + '\n This is email that I am sending from Python! \n\n'
smtpserver.sendmail(gmail_user, to, msg)
print('done!')
smtpserver.close()
quit()

