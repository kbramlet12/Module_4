# Program Name: branching.py
# Purpose of a program: A time traveler has suddenly appeared in your classroom!
# The travelor enters his/her year of origin
# Program returns a greeting message according to the year.  ### THIS IS THE EXPECTED OUTPUT
# Distant Past: Before 1900
# Present Era-Years between 1900-2020
# Far Future: After 2020

year = int(input("Greetings! What is your year of origin?"))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
elif year > 2020:
    print ("Far out, that's the future!!")

#1 The first thing I did was run the program to see if it was producing the expected output or not given specific inputs. 
#2 The first error was a syntax error in line 9, so I fixed that, and ran again.
#3 Another one in line 12! I almost couldn't detect the single apostrophe in the begining of the line.
#4 Had to fix the missing ":" after 1900
#5 Double "&"
#6 Needed to fix the future IF statement
#7 It ran but the print screen said year was not defined, I changed the first line of code to hopefully fix that.
#8 It almost worked! the last thing I needed to do was change the "&" to "and" and the future years actually displayed the proper outputs! 
#AUTHOR: Keegan Bramlet
#DATE: 10/30/2022
