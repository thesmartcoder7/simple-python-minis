# for this simple application, you need to add birthdays to the csv file using the proper format.

import smtplib
import datetime as dt
import random
import pandas
import os

today = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
birth_date_list = data.day.to_list()
birth_month_list = data.month.to_list()

if today.day in birth_date_list and today.month in birth_month_list:
    path = 'letter_templates'
    files = os.listdir(path)
    generated_file = random.choice(files)
    birth_name_list = data[data.day == today.day].name.to_list()
    email_list = data[data.day == today.day].email.to_list()
    birthday_dictionary = dict(zip(birth_name_list, email_list))

    for recipient in birth_name_list:
        email = birthday_dictionary[recipient]
        with open(f"{path}/{generated_file}", mode="r") as f:
            data = f.readlines()
            message = ""
            for lines in data:
                message += lines
            message = message.replace("[NAME]", recipient)

            sender = "your email"
            my_password = "your password"
            receiver = email
            subject = "Its Your Birthday!!!"
            with smtplib.SMTP("your domain name / smtp name ") as connection:
                connection.starttls()
                connection.login(user=sender, password=my_password)
                connection.sendmail(
                    from_addr=sender,
                    to_addrs=receiver,
                    msg=f"Subject: {subject}\n\n{message}"
                )
                print(f"Email to {recipient} has been successfully sent!")
