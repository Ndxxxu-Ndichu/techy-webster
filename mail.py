import smtplib, ssl
from email.mime.text import MIMEText

def send_mail(name, email, message):
    port = 587
    smtp_server = 'smtp.gmail.com'
    login = 'ndichumwangi7@gmail.com'
    password = 'vgqsqwbjflfmafqj'
    message = f"<h3>New Portfolio Client</h3>" \
              f"<ul><li>Name: {name}</li>" \
              f"<li>Email: {email}</li>" \
              f"<li>Message: {message}</li></ul>"

    sender_email = f'{email}'
    reciever_email = 'ndichumwangi7@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'New Portfolio Contact'
    msg['From'] = sender_email
    msg['To'] = reciever_email

    context = ssl.create_default_context()
    #send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(login, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())