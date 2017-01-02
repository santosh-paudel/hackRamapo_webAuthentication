MONGO_DBNAME='hackRamapo'
MONGO_URL='mongodb://localhost:27017/hackRamapo'

TWILIO_SID=os.environ.get('TWILIO_SID')
TWILIO_AUTH_TOKEN=os.environ.get('TWILIO_AUTH_TOKEN')

MAIL_SERVER='smtp.googlemail.com'
MAIL_PORT=465
MAIL_USE_SSL=True
MAIL_USE_TSL=False
FLASK_ADMIN=os.environ.get('MAIL_USERNAME')
MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')