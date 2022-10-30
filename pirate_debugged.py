# Program Name: pirate.py
# Purpose of a program:
# User can be screened by the greeting message user enters as: a pirate or pirate hater
# Pirates greet each other with a password.
# If the greeting is matched to Arrr!,the user is identified as a pirate.
# Otherwise, the user is a hater of pirates.

greeting = input("Hello, possible pirate! What's the password?")
password = "Arrr!"
if greeting == password:
    print("Greetings, matey!")
else:
    print("Be gone, hater of pirates!")

#1 First I fixed some formatting to see If I could get the expected output
#2 Then I changed some words/phrases around so the outputs made sense in the context of what the program should do
#3 It works!
#AUTHOR: Keegan Bramlet
#DATE: 10/30/2022
