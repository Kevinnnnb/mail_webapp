import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail(ton_email, mot_de_passe, destinataire, sujet, body):
    html_message = MIMEText(body, 'html')
    html_message['sujet'] = sujet
    html_message['From'] = ton_email
    html_message['To'] = destinataire
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(ton_email, mot_de_passe)
        server.sendmail(ton_email, destinataire, html_message.as_string())

    print('Email envoyé !')

ton_email = 'yourname@mail.com'
mot_de_passe = 'your security key' #Qui se trouve dans les paramètres gmail : si jamais y'a des sueper tutos d'indien sur Youtube ...
destinataire = 'yourname@mail.com'
sujet = 'Hello World !'
body = ''' Your content here ! '''

#Envoie de l'email
mail(ton_email, mot_de_passe, destinataire, sujet, body)
