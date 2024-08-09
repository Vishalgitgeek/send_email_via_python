# Automated Email Sender
A Python project to automate the process of sending emails using `smtplib`.


## Description
The Automated Email Sender is a Python program that simplifies the process of sending emails to multiple recipients. 
It's ideal for sending newsletters, announcements, or any bulk emails with customized content.

## Features
- Send personalized emails to multiple recipients.
- Supports HTML and plain text emails.
- Secure authentication using SSL/TLS.


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vishalgitgeek/send_email_via_python/tree/main
   cd send_email_via_python
   ```

2. **Install required libraries:**
   
   install smptlib, pandas
   command:
   pip install pandas
   pip install smptlib

3. **Set up environment variables:**
   ```bash
   replace the email.csv file with your .csv file with column name :- name & email
   inside mssg.txt file , write your massge , don't change the first line
   inside main.py file replace subject with actual subject of your email

5. **Run the program:**
   ```bash
   python send_email.py
   ```

### 6. **Usage**
```markdown
## Usage
1. Open the `send_email.py` file and modify the recipient list and message content as needed.
2. Run the script using the command:
   ```bash
   python send_email.py
3. NOte:
  inside main.py don't use your original email password ,instead goto your gmail/yahoo/hotmail and then to account setting
  search for app password and gererate a password from there and paste the password or assign the password to my_password variable
   ```





