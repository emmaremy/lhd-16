from datetime import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
import email as emailLIB
import re

def is_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

def send_email(from_email, to_email, subject, text, png_filename):
    serverIP="127.0.0.1"

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(png_filename, "rb").read())
    Encoders.encode_base64(part)

    part.add_header('Content-Disposition', 'attachment; filename={}'.format(png_filename))

    msg.attach(part)

    server = smtplib.SMTP(serverIP)
    server.sendmail(from_email, to_email, msg.as_string())

def get_time(timestr):
    date_object = datetime.strptime(timestr, '%a, %d %b %Y %H:%M:%S %z')
    return date_object
