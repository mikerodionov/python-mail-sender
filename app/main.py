import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

def readCsv(filePath, hasHeader=False):
    contacts = []
    with open(filePath, mode='r', newline='', encoding='utf-8') as csvfile:
        if hasHeader:
            reader = csv.DictReader(csvfile)
        else:
            reader = csv.reader(csvfile)
            for row in reader:
                contacts.append({
                    'name': row[0],
                    'email': row[1]
                })
            return contacts

        for row in reader:
            contacts.append({
                'name': row['name'],
                'email': row['email']
            })
    
    return contacts

# Example usage
# filePath = '../data/sample.csv'
# contactsWithoutHeader = readCsv(filePath)

# print("Contacts without header:", contactsWithoutHeader)

def readTemplate(templatePath):
    with open(templatePath, 'r', encoding='utf-8') as templateFile:
        template = templateFile.read()
    return template

def prepareMailBody(contact, templatePath):
    template = readTemplate(templatePath)
    mailBody = template.replace('<NAME>', contact['name'])
    return mailBody

# Example usage
# filePath = '../data/sample.csv'
# contactsWithoutHeader = readCsv(filePath)
# templatePath = '../data/template.txt'
# for contact in contactsWithoutHeader:
#     mailBody = prepareMailBody(contact, templatePath)
#     print(mailBody)
#     print('---')  # Separator for readability

def sendEmail(subject, body, to_email, from_email, smtp_password):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Example usage
filePath = '../data/sample.csv'
templatePath = '../data/template.txt'
subject = "Job Application"

from_email = input("Enter your Gmail address: ").strip()
smtp_password = getpass.getpass("Enter your Gmail password: ")

contactsWithoutHeader = readCsv(filePath)

for contact in contactsWithoutHeader:
    mailBody = prepareMailBody(contact, templatePath)
    print(mailBody)
    print('---')  # Separator for readability
    
    send_prompt = input(f"Do you want to send this email to {contact['name']} at {contact['email']}? (yes/no): ").strip().lower()
    if send_prompt == 'yes':
        sendEmail(subject, mailBody, contact['email'], from_email, smtp_password)