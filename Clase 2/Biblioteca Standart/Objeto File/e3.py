import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "codigodata@gmail.com"
toaddr = "carlosblancogomez69@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE EMAIL"
 
body = "TEXT YOU WANT TO SEND"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "python-logo.png"
attachment = open(filename, "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "alzamanito")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()