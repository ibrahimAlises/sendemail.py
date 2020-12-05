import smtplib, ssl
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEultipart
from email.mime.base import MIMEBase
from email import encoders 

sender_email = "(CHANGENAME)"
receiver_email = "(CHANGENAME)"

message = MIMEultipart("")
messgae["subject"] = "[CHANGENAME]"
message["From"] = sender_email
message ["To"] = receiver_email 

text = """\
Mesaj
"""

part1 = MIMEText(text, "plain")
message.attach(part1)

filepath = "[CHANGENAME]"
part2 = MIMEBase('application', "octet-stream")
part2.set_payload(open(filepath, "rb").read()
encoders.encode_base64(part2)
              
part2.add_header('content-Disposition', 'attachment; filename"[CHANGENEME]"')              

message.attach(part2)

# create secure connection with server and send email
context = ssl.create_default_context()
server = smtplib.SMTP("SMTP_DOMAİN",PORT)
server.starttls()
server.ehlo_or_helo_if_needed()
server.sendemail(
        sender_email, receiver_email, message.as_string()
  )
