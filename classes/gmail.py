import smtplib
import datetime
from email.mime.multipart import MIMEMultipart


class Gmail:
    def __init__(self):
        return

    def send_email(self, body):
        try:
            # Gmail account authentication
            gmail_user = '' # Insert your gmail address
            gmail_password = '' # Insert your gmail app password

            # Set email configuration
            msg = MIMEMultipart('alternative')
            msg.attach(body)
            msg['From'] = '' # Insert from address
            msg['To'] = '' # Insert to address
            now = datetime.datetime.now()
            msg['Subject'] = str(now.month) + '-' + str(now.day) + '-' + str(now.year) + ' Stock Insights'

            # Send email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(gmail_user, gmail_password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.close()

        except Exception as e:
            # Print thrown error
            print(str(e))
