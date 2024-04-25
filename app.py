from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Konfiguration für Flask-Mail
app.config['MAIL_SERVER'] = 'posteo.de'  # SMTP-Server für Posteo
app.config['MAIL_PORT'] = 465  # Port für den SMTP-Server mit SSL
app.config['MAIL_USE_TLS'] = False  # TLS-Verschlüsselung deaktivieren
app.config['MAIL_USE_SSL'] = True  # SSL-Verschlüsselung aktivieren
app.config['MAIL_USERNAME'] = 'm.lenzen@posteo.de'  # Posteo E-Mail-Adresse
app.config['MAIL_PASSWORD'] = 'Gudi1269u6'  # Posteo E-Mail-Passwort

mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/references')
def references():
    return render_template('references.html')

@app.route('/imprint')
def imprint():
    return render_template('imprint.html')

@app.route('/datenschutz')
def datenschutz():
    return render_template('datenschutz.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # E-Mail senden mit sicherer Absenderadresse
    msg = Message('Neue Nachricht von {}'.format(name), sender=app.config['MAIL_USERNAME'], recipients=['m.lenzen@posteo.de'])
    msg.body = message
    with mail.connect() as conn:  # Explizite Verbindung
        conn.send(msg)
    
    return 'Nachricht erfolgreich gesendet!'

if __name__ == '__main__':
    app.run(debug=True)

