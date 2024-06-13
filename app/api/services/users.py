import os
import smtplib

from dotenv import load_dotenv
from email.mime.text import MIMEText


class UserService():
    
    def send_email(self, email_to: str):
        load_dotenv()
        
        smtp_server = os.getenv('EMAIL_SERVER')
        smtp_port = os.getenv('EMAIL_PORT')
        username = os.getenv('EMAIL_USERNAME')
        password = os.getenv('EMAIL_PASSWORD')
        if email_to is None:
            email_to = os.getenv('EMAIL_USERNAME')
        message = MIMEText('tTexto')
        
        message['Subject'] = 'Asunto'
        message['From'] = username
        message['To'] = email_to
        try:
            smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
            smtp_connection.starttls()
            smtp_connection.login(username, password)
        except Exception as e:
            return False, e
        finally:
            smtp_connection.sendmail(username, message['To'], message.as_string())
            smtp_connection.quit()
            return True, 'Email send'