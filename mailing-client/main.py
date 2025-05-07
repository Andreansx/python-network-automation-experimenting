import smtplib
import email.mime.text
import email.mime.multipart
import email.mime.base
import ssl  
server = smtplib.SMTP("smtp.gmail.com", 25)
server.ehlo()

print("reading password and mail address from files now...")
with open("password.txt", "r") as passfile:
    password = passfile.read()
with open("mailaddr.txt", "r") as mailfile:
    mailaddr = mailfile.read()
server.login(mailaddr, password)

print("password and mail address read successfully")

msg = email.mime.multipart.MIMEMultipart()
msg["From"] = mailaddr
msg["To"] = mailaddr
msg["Subject"] = "Test email"
with open("body.txt", "r") as body:
    msg.attach(email.mime.text.MIMEText(body.read()))
