from decouple import config

class Config:
    NEWS_API_KEY = config('NEWS_API_KEY')
    EMAIL_ADDRESS = config('EMAIL_ADDRESS')
    EMAIL_PASSWORD = config('EMAIL_PASSWORD')
    SMTP_SERVER = config('SMTP_SERVER', default='smtp.gmail.com')
    SMTP_PORT = config('SMTP_PORT', default=587, cast=int)