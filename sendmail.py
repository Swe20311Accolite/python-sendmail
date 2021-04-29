import smtplib
from email import encoders
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

sm = smtplib.SMTP('smtp.gmail.com',587)
sm.starttls()
sender = input ("enter sender email: ")
password = getpass()
receiver = input ("enter receiver email: ")
sm.login (sender,password)
Text = MIMEMultipart()
Text["Subject"] ="Hello User"
Text["From"] = sender
Text["To"] = receiver

#body = """Welcome to zomato"""

htmlBody="""
<html>
    <body>
        <p>welcome bruh</p>
    </body>
</html>
"""
#p=MIMEText(body,"plain")
p1=MIMEText(htmlBody,"html")

file1 ="image.jpg"
imagefile=open(file1,"rb")
p3=MIMEBase("image","jpg")
p3.set_payload((imagefile).read())
encoders.encode_base64(p3)
p3.add_header('Content-Disposition',"imagefile; filename=%s" % file1)

csv_files = ["contacts.csv","contacts1.csv"]
for files in csv_files:
    f = open(files,"rb")
    p=MIMEBase("text","csv")
    p.set_payload((f).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition',"f; filename=%s" % files)
    Text.attach(p)

Text.attach(p1)
Text.attach(p3)
sm.sendmail(sender,receiver.split(","),Text.as_string())
print("mail sent")
sm.quit()
