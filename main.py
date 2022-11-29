
import smtplib
import imghdr
from email.message import EmailMessage


login = "i@olaoluwasubomi.com"
password = input("Type your password and press enter:")
Reciever_Email = "subo@subxmi.com"
port = 587  # For starttls
smtp_server = "smtp.gmail.com"

message = """Subject: Model Submissions
To: {recipient}
From: {sender}

Hi {name}, 
My Name is Olaoluwasubomi Aduloju
I Live in Brooklyn, NY
I am 6'05 Ft Tall
I am 18 Years Old
Sophomore in College
Waist is 29.5
Shoe Size is 43.5
instagram: @subxmi
twitter @sxbxmi
tiktok @subospersona
"""





with smtplib.SMTP(smtp_server, port) as server:
    server.connect('smtp.gmail.com', '587')
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted   
    server.login(login, password)
    
    with open("contacts.csv") as file:
            reader = csv.reader(file)
            next(reader)  # it skips the header row
            for name, email in reader:
                    server.sendmail(
                    sender,
                    email,
                    message.format(name=name, recipient=email, sender=sender)
                )
            print(f'Sent to {name}')