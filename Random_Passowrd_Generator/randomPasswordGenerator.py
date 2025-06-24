# random password generator
import random
import string
password = "" #take an empty string
characters = string.ascii_letters + string.digits + string.punctuation
length = int(input("Enter the length of password: "))
for i in range(length):
   password += random.choice(characters) #to append characters one by one
print("your password is: " + password)