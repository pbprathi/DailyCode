import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_add="bhageerath@prathi.com"
to_add="pbprathi@gmail.com"

msg=MIMEMultipart()

msg['From']=from_add
msg['To']=to_add
msg['Subject']=("This is an Important message")

body=('This is a test mail sending using python')

msg.attach(MIMEText(body,('plain')))

# Code for attaching a file.
filename='screen.jpg'
attachment=open("/home/bhageerath/pythontuts/projects/textprocessing/screen.jpg","rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('pbprathi','Shyam123')

text=msg.as_string()
server.sendmail(from_add,to_add,text)
server.quit()
