from datetime import datetime
import smtplib
import base64
import re

def is_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

def send_email(from_email, to_email, subject, text, png_filename):
    serverIP='localhost'

    fo = open(png_filename, "rb")
    filecontent = fo.read()
    encodedcontent = base64.b64encode(filecontent)

    sender = from_email
    reciever = to_email

    marker = "AUNIQUEMARKER"

    body = text

    part1 = """From: HealthyText <%s>
    To: You <%s>
    Subject: HealthyText Summary
    MIME-Version: 1.0
    Content-type: multipart/mixed; boundary=%s
    --%s
    """% (marker, marker, from_email, to_email)

    part2 = """Content-type: text/plain
    Content-Transfer-Encoding:8bit

    %s
    --%s
    """% (body, marker)

    part3 = part3 = """Content-Type: multipart/mixed; name=\"%s\"
    Content-Transfer-Encoding:base64
    Content-Disposition: attachment; filename=%s

    %s
    --%s--
    """ %(png_filename, png_filename, encodedcontent, marker)

    message = part1 + part2 + part3

    try:
      server = smtplib.SMTP(serverIP)
      server.sendmail(from_email, to_email, msg.as_string())
    except Exception:
      print "Error: unable to send email"

def get_time(timestr):
    date_object = datetime.strptime(timestr, '%a, %d %b %Y %H:%M:%S %z')
    return date_object

#def main():
#  send_email('test@gmail.com', 'eremy1@swarthmore.edu', "TEST", "TEST CONTENT", "./apple_raw.png")

#main()
