#this program shows number of days in a month
# Author: wasaif Diab
# Date: 29/12/2025

month = input("Enter the month numper (1-12): ")

if month==2:
    print("28 or 29 days")
elif month==4 or month==6 or month==9 or month==11:
    print("30 days")
else:
    print("31 days")
