from flask import Flask, render_template, request, jsonify, send_file

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



app = Flask(__name__)

# Email Configuration - Define these directly since we're not using environment variables
SENDER_EMAIL = "varupulaavanthi@gmail.com"
SENDER_PASSWORD = "ncrg bzai bswr suvl"

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject', 'Contact Form Submission')
        message = request.form.get('message')

        if not all([name, email, message]):
            return jsonify({
                "status": "error",
                "message": "Please fill in all required fields."
            })

        # Create message for portfolio owner
        msg_to_owner = MIMEMultipart()
        msg_to_owner['From'] = SENDER_EMAIL
        msg_to_owner['To'] = SENDER_EMAIL
        msg_to_owner['Subject'] = f"Portfolio Contact: {subject}"

        # Email body for portfolio owner
        owner_body = f"""
        New message from your portfolio website:
        
        Name: {name}
        Email: {email}
        Subject: {subject}
        Message: {message}
        """
        msg_to_owner.attach(MIMEText(owner_body, 'plain'))

        # Create confirmation message for sender
        msg_to_sender = MIMEMultipart()
        msg_to_sender['From'] = SENDER_EMAIL
        msg_to_sender['To'] = email
        msg_to_sender['Subject'] = "Thank you for contacting Avanthi Varupula"

        # Email body for sender
        sender_body = f"""
        Dear {name},

        Thank you for contacting me through my portfolio website. I have received your message and will get back to you soon.

        Here's a copy of your message:
        
        Subject: {subject}
        Message: {message}

        Best regards,
       varupulaavanthi
        """
        msg_to_sender.attach(MIMEText(sender_body, 'plain'))

        # Send emails
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            # Send to portfolio owner
            server.send_message(msg_to_owner)
            # Send confirmation to sender
            server.send_message(msg_to_sender)

        return jsonify({
            "status": "success",
            "message": "✨ Thank you for your message! I'll get back to you soon! ✨"
        })
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return jsonify({
            "status": "error",
            "message": "Failed to send message. Please try again later."
        })

@app.route('/download_resume')
def download_resume():
    try:
        return send_file(
            'static/resume/resume.pdf',  # Path to your resume file
            as_attachment=True,
            download_name='Avanthi_Varupula_Resume.pdf'
        )
    except Exception as e:
        print(f"Error downloading resume: {str(e)}")
        return "Resume not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT', 5000))
