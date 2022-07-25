from http import server
import smtplib
import os
from email.mime.text import MIMEText


def send_email(message):
    sender = "keannko@gmail.com"
    password = "wrysogwylbuqmfic"

    mail_to = "keannko@bigmir.net"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Click me please!"
        server.sendmail(sender, mail_to, msg.as_string())

        return "The message was sent successfully"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def main():
    message = input("Type your message: ")
    print(send_email(message=message))


if __name__== '__main__':
    main()