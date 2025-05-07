import smtplib

server = smtplib.SMTP("smtp.gmail.com", 25)
server.ehlo()

with open("password.txt", "r") as passfile:
    password = passfile.read()
with open("mailaddr.txt", "r") as mailfile:
    mailaddr = mailfile.read()
server.login(mailaddr, password)
