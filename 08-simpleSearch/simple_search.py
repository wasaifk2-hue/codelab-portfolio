#this program searches for a number in a list
# Author: wasaif Diab
# Date: 29/12/2025

numbers=[5, 8, 12, 20, 25, 30]
search=int(input("Enter  number to search  "))
if search in numbers:
    print("Number found")
else:
    print("Number not found")
