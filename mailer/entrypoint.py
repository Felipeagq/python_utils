import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

s = smtplib.SMTP(
    host="smtp.gmail.com",
    port=587
)
s.starttls()
s.login(
    user="no-reply@feanware.com",
    password="CONTRASEÑA"
)
msg = MIMEMultipart()

msg["From"]= "no-reply@feanware.com"
msg["To"]="felipeagq99@gmail.com"
msg["Subject"]="Test2 gmail"

message = "Mensaje de prueba desde codigo"

msg.attach(MIMEText(message,"plain"))

s.send_message(msg)

s.quit()