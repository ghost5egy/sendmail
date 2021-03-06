from smtplib import SMTP
import email.message
import re


def sendmailg(gserver , gport ,guser, gpass , mailfrom , mailto , subject , msg , ishtml = 0):
    mailmsg = email.message.Message()
    mailmsg['From'] = mailfrom
    mailmsg['To'] = mailto
    mailmsg['Subject'] = subject

    if ishtml == 1:
        mailmsg.add_header('Content-Type','text/html')
    else:
        mailmsg.add_header('Content-Type','text/plain')

    mailmsg.set_payload (msg, 'utf-8')
    with SMTP(gserver , gport)  as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(guser, gpass)  
        smtp.set_debuglevel(1)
        smtp.sendmail(mailfrom, mailto,mailmsg.as_string())
        smtp.quit()

gserver = 'smtp.smtpserver.com'
gport = 587 # or 25 whatever you use 
guser = ''
gpass = ''
mailfrom = 'test@test.com'
mailto = 'test1@test.com,test2@test.com'
subject = 'test'
msg = "<html><head></head><body><a href=\"http://www.example.com/\">Please Click the link :)</a></body></html>"
sendmailg(gserver , gport , guser, gpass , mailfrom , mailto , subject , msg , 1)
