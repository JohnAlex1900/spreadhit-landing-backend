from flask import jsonify, request
from flask_mail import Mail, Message
import os

from flask import Flask

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.zoho.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'info@spreadhit.com'
app.config['MAIL_PASSWORD'] = os.getenv('ZOHO_MAIL_PASSWORD')  # Store password in environment variable
app.config['MAIL_DEFAULT_SENDER'] = 'info@spreadhit.com'

mail = Mail(app)


@app.route('/send_confirmation_email', methods=['POST'])
def send_confirmation_email():
    data = request.get_json()
    name = data['name']
    email = data['email']

    try:
        msg = Message(
            "Thank you for joining the waitlist!",
            recipients=[email],
        )
        msg.body = f"Hi {name},\n\nThank you for joining the waitlist! Our product is coming soon and you'll be the first to know!\n\nBest regards,\nThe SpreadHit Team"

        mail.send(msg)
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        print(f"Failed to send email: {e}")
        return jsonify({"message": "Error sending email"}), 500
