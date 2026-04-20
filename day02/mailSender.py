import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText


def send_email():
    sender = sender_entry.get().strip()
    password = password_entry.get().strip()
    receiver = receiver_entry.get().strip()
    subject = subject_entry.get().strip()
    body = body_text.get("1.0", tk.END).strip()

    if not sender or not password or not receiver or not subject or not body:
        messagebox.showwarning("Missing Info", "Please fill all fields!")
        return

    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver

        # Gmail SMTP Server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()

        messagebox.showinfo("Success", "Email sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email:\n{e}")


# GUI Window
root = tk.Tk()
root.title("Simple Mail Sender")
root.geometry("450x500")

# Labels & Inputs
tk.Label(root, text="Sender Email:").pack(pady=5)
sender_entry = tk.Entry(root, width=50)
sender_entry.pack()

tk.Label(root, text="Sender Password (App Password recommended):").pack(pady=5)
password_entry = tk.Entry(root, width=50, show="*")
password_entry.pack()

tk.Label(root, text="Receiver Email:").pack(pady=5)
receiver_entry = tk.Entry(root, width=50)
receiver_entry.pack()

tk.Label(root, text="Subject:").pack(pady=5)
subject_entry = tk.Entry(root, width=50)
subject_entry.pack()

tk.Label(root, text="Message:").pack(pady=5)
body_text = tk.Text(root, width=50, height=10)
body_text.pack()

# Send Button
send_btn = tk.Button(root, text="Send Email", command=send_email, bg="green", fg="white", padx=10, pady=5)
send_btn.pack(pady=15)

root.mainloop()