import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client


sender_email = 'dev.elcruzo@gmail.com'
sender_password = 'your_app_password'


twilio_account_sid = 'your_twilio_account_sid'
twilio_auth_token = 'your_twilio_auth_token'
twilio_phone_number = '+1234567890'  # Your Twilio phone number


twilio_client = Client(twilio_account_sid, twilio_auth_token)


def send_email(product, user_email):
    subject = 'Price Alert: {} - ${}'.format(product.name, product.current_price)
    message = 'The price of {} has dropped to ${}!'.format(product.name, product.current_price)


    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = user_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, user_email, msg.as_string())
        server.quit()
    except Exception as e:
        print('Error sending email:', str(e))

# Function to send SMS notification
def send_sms(product, user_phone):
    message = 'Price alert for {}: Current price is ${}, below your threshold of ${}'.format(product.name, product.current_price, product.target_price)
    
    try:
        twilio_client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=user_phone
        )
    except Exception as e:
        print('Error sending SMS:', str(e))