# sendmail
sendmail using stmplib 

the way to edit the function is :

gserver : is the server you want use to send mail .\n

gport : the port of the smtp service .\n

guser : the user of the service .\n

gpass : the password of the service .\n

mailfrom : the sender mail .\n

mailto : the reciver of the mail .\n

msg : the message body that will be sent .\n

ishtml : if the msg body is html set that value to 1 else leave it blank .\n

sendmailg(gserver , gport , guser, gpass , mailfrom , mailto , msg , ishtml)
