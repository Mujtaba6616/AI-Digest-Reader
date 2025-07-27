import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class EmailSender:
    def __init__(self, config):
        self.config = config
    
    def send_digest(self, recipient, digest_html):
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f"📰 Daily News Digest - {datetime.now().strftime('%Y-%m-%d')}"
            msg['From'] = self.config.EMAIL_ADDRESS
            msg['To'] = recipient
            
            # Attach HTML content
            html_part = MIMEText(digest_html, 'html')
            msg.attach(html_part)
            
            # Send email
            with smtplib.SMTP(self.config.SMTP_SERVER, self.config.SMTP_PORT) as server:
                server.starttls()
                server.login(self.config.EMAIL_ADDRESS, self.config.EMAIL_PASSWORD)
                server.send_message(msg)
            
            print(f"✅ Email sent to {recipient}")
            
        except Exception as e:
            print(f"❌ Email error: {e}")