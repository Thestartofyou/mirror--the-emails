import imaplib
import email
from email.header import decode_header

# Email account credentials
username = "your_email@example.com"
password = "your_password"
imap_server = "imap.example.com"

# Connect to the server
mail = imaplib.IMAP4_SSL(imap_server)

# Login to your account
mail.login(username, password)

# Select the mailbox you want to use
mail.select("inbox")

# Search for all emails in the inbox
status, messages = mail.search(None, "ALL")

# Convert messages to a list of email IDs
email_ids = messages[0].split()

# Fetch the latest email
latest_email_id = email_ids[-1]
status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

# Extract the email message
msg = email.message_from_bytes(msg_data[0][1])

# Decode the email subject
subject, encoding = decode_header(msg["Subject"])[0]
if isinstance(subject, bytes):
    subject = subject.decode(encoding if encoding else "utf-8")

# Print the subject
print("Subject:", subject)

# Logout from the server
mail.logout()
