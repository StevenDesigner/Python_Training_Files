# import smtplib

# my_email="samplepython@hotmail.com"
# password="r%u.%5*LpG8Y9,m"

# with smtplib.SMTP("smtp-mail.outlook.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="stephenrajprime@gmail.com",
#                         msg="Subject:Sample Mail \n\nhi")


import smtplib
import datetime as dt
import random

MY_EMAIL = "samplepython@hotmail.com"
MY_PASSWORD = "r%u.%5*LpG8Y9,m"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="stephenrajprime@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
