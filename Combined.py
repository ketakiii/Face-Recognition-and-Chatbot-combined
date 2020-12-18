import pandas as pd
from face import faces
import csv

print("Select 1 for : Face Recognition and viewing information, 2 for: Entering a new person's information and 3 for: "
      "interacting with the Chat bot for doubts")
inp = input("Enter your choice: ")

if inp == "1":
    print("ppp")
    faces()

else:
    if inp == "2":

        print("Enter your details below.")
        name = input("Enter your name: ")
        rollno = int(input("Enter you roll no: "))
        grno = input("Enter your GR No: ")
        add = input("Enter you address: ")
        email = input("Enter your E-mail id: ")
        phone = input("Enter you Mobile number :")
        a = len(phone)
        if (a > 10 or a < 10):
            print("Enter only a 10 digit phone no")
            input("Enter you Mobile number :")

        with open('mycsv.csv', 'a', newline='') as f:
            thewriter = csv.writer(f)
            thewriter.writerow([name, rollno, grno, add, phone, email])



    else:
            if inp == "3":
                from chatbot import chat
                chat()
