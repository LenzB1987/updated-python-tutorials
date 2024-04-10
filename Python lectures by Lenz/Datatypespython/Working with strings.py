#strings are usuallly detonated by single quotes '' or double quotes ""
# strings are a collection of text and characters 
# description of a string
name='lenz'
country='uganda'
status='9completed'
#it should be noted that strings must not  be reserved words
#this will confusse the compiler
# how to display strings
print(name)
print(country)
print(status)
# you can use the print formating
text= "The country is {country}, his name is {name}, his status is {status}".format(country="Uganda", name="lenz", status="single")
print(text)
#or 
text2="The country is {0},his name is {1}, his status is {2}".format("Uganda","Lenz","single")
print(text2)
#or method 3
text3="The country is {}, his name is {}, his status is {}".format("Uganda","Lenz","single")
print(text3)
import sys
print(sys.version)