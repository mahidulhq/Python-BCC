# Simple Mail Sender (Tkinter + Gmail SMTP)

A lightweight desktop app built with Python and Tkinter to send plain-text emails through Gmail SMTP.

## Overview

This project provides a small GUI where you enter:

- Sender email
- Sender app password
- Receiver email
- Subject
- Message body

When you click **Send Email**, the app connects to Gmail SMTP using TLS, authenticates, and sends the message.

## How It Works

1. The GUI collects input values from Tkinter Entry/Text fields.
2. Basic validation checks that all fields are filled.
3. The app builds an email using `MIMEText`.
4. It connects to Gmail SMTP server: `smtp.gmail.com` on port `587`.
5. TLS is started with `starttls()`.
6. Login is performed with sender email + app password.
7. Email is sent using `server.sendmail(...)`.
8. A success or error popup is shown using Tkinter message boxes.

## Project Structure

- `emailSender.py`: Main application (GUI + email sending logic).

## Requirements

- Python 3.8+ (recommended)
- Internet connection
- Gmail account with:
  - 2-Step Verification enabled
  - App Password generated for Mail

No third-party packages are required. The script uses only Python standard library modules:

- `tkinter`
- `smtplib`
- `email.mime.text`

## Setup

1. Make sure Python is installed.
2. Open a terminal in the project folder.
3. (Optional) Create and activate a virtual environment.

## Run the App

```bash
python emailSender.py
```

## Usage

1. Enter your sender Gmail address.
2. Enter your Gmail App Password (not your normal Gmail password).
3. Enter the receiver email address.
4. Enter a subject.
5. Enter the message text.
6. Click **Send Email**.

If successful, you will see: **Email sent successfully!**

## Gmail App Password Guide

Gmail often blocks normal account passwords for SMTP apps.

To create an App Password:

1. Enable 2-Step Verification on your Google account.
2. Go to Google Account settings -> App Passwords.
3. Create a new App Password for Mail.
4. Use that generated password in this app.

## Error Handling

The app currently handles:

- Missing input fields (shows a warning)
- SMTP/login/network errors (shows detailed error popup)

## Security Notes

- Do not hardcode email credentials in source code.
- Do not share or commit real passwords.
- Prefer using environment variables or secure credential storage for production apps.

## Limitations

- Sends plain-text email only (no HTML formatting).
- Sends to one receiver at a time.
- Gmail SMTP specific settings are hardcoded.

## License

This project is for learning and educational use.
