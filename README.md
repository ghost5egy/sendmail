# sendmail
sendmail using stmplib 

the way to edit the function is :

gserver : is the server you want use to send mail 
gport : the port of the smtp service 
guser : the user of the service 
gpass : the password of the service 
mailfrom : the sender mail 
mailto : the reciver of the mail 
msg : the message body that will be sent 
ishtml : if the msg body is html set that value to 1 else leave it blank

sendmailg(gserver , gport , guser, gpass , mailfrom , mailto , msg , ishtml)
