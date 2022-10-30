# Program Name: time2.py
# Purpose of a program:
# User inputs current time and hours to wait.
# Then program returns the time user's waiting time ends.

str_time = input("What hour is it now from 0 to 24?")
str_wait_time = input("What is the number of hours to wait?")
time = int(str_time)
wait_time = int(str_wait_time)

time_to_start = (time + wait_time) % 24
print("Start Time:", time_to_start) 

#1 I fixed some basic spelling errors and decided to run it to see what happened
#2 I added the %24 so it would print the remainder after 24 hrs
#3 It Works!
#AUTHOR: Keegan Bramlet
#DATE: 10/30/2022
