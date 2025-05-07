import smtplib
import email.mime.text
import email.mime.multipart
import email.mime.base
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.ehlo()
print("reading password and mail address from files now...")
with open(os.path.join(BASE_DIR, 'password.txt'), "r") as passfile:
    password = passfile.read().strip()
with open(os.path.join(BASE_DIR, 'mailaddr.txt'), "r") as mailfile:
    mailaddr = mailfile.read().strip()
try:
    server.login(mailaddr, password)
except smtplib.SMTPAuthenticationError as e:
    print("Authentication failed: Application-specific password may be required. Please refer to https://support.google.com/mail/?p=InvalidSecondFactor")
    raise e

msg = email.mime.multipart.MIMEMultipart()
msg["From"] = mailaddr
msg["To"] = mailaddr
msg["Subject"] = "Test email"
with open("body.txt", "r") as body:
    msg.attach(email.mime.text.MIMEText(body.read()))

with open("image.png", "rb") as img:
    part = email.mime.base.MIMEBase("application", "octet-stream")
    part.set_payload(img.read())
    email.encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename=image.png")
    msg.attach(part)

print("sending email now...")
try:
    server.sendmail(mailaddr, mailaddr, msg.as_string())
    print("email sent successfully")
except Exception as e:
    print(f"error sending email: {e}")
finally:
    server.quit()
    print("server quit successfully")   

