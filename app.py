from flask import Flask, render_template, request, jsonify, send_file
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

app = Flask(__name__)

# Email Configuration
SENDER_EMAIL = "varupulaavanthi@gmail.com"  # Your email
SENDER_PASSWORD = "cfrb qtar nyfu vtkw"      # Your app password
RECEIVER_EMAIL = "varupulaavanthi@gmail.com"  # Where you want to receive msgs

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
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # Validate required fields
        if not all([name, email, message]):
            return jsonify({
                "status": "error",
                "message": "Please fill in all required fields."
            })

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = f"Portfolio Contact Form: Message from {name}"

        # Format email body with timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        body = f"""
        New message received from your portfolio website:

        Timestamp: {current_time}
        
        Sender Details:
        ---------------
        Name: {name}
        Email: {email}
        Phone: {phone if phone else 'Not provided'}
        
        Message:
        --------
        {message}
        """

        msg.attach(MIMEText(body, 'plain'))

        # Setup SMTP server and send email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)

        return jsonify({
            "status": "success",
            "message": "Thank you! Your message has been sent successfully."
        })

    except Exception as e:
        print(f"Error sending email: {str(e)}")  # For debugging
        return jsonify({
            "status": "error",
            "message": "Sorry, there was an error sending your message. Please try again later."
        })

@app.route('/download_resume')
def download_resume():
    try:
        return send_file(
            'static/resume/resume.pdf',  # Make sure this path is correct
            as_attachment=True,
            download_name='Avanthi_Varupula_Resume.pdf'
        )
    except Exception as e:
        print(f"Error downloading resume: {str(e)}")  # For debugging
        return "Resume not found", 404

if __name__ == '__main__':
    app.run(debug=True)
