import smtplib
import pandas as pd

# reading data from csv file
data = pd.read_csv("emails.csv")

# from data, getting user details(name and emails)
user_details = [[data['name'], data['email']] for index, data in data.iterrows()]

# this is sender's email and password
my_email = "your email (sender's email)"
my_password = "XXXXX XXXXX XXXXX XXXXX"  # don't use your original password ,
# instead goto my account and search "app password" and generate a password which you will be using here

# opening mssg file where your mail is saved(in txt file)
file = f"mssg.txt"
message = open(file, 'r').read()

# creating connections with smtplib
with smtplib.SMTP("smtp.gmail.com") as connections:
    connections.starttls()  # this creates a secured connections
    connections.login(my_email, my_password)  # python will login with my email and password
    for i in range(len(user_details)):
        message = message.replace("[NAME]", str(user_details[i][0]))
        connections.sendmail(from_addr=my_email,
                             to_addrs=user_details[1],
                             msg=f"Subjects: subject\n\n{message}") # replace 'subject' with actual subject


