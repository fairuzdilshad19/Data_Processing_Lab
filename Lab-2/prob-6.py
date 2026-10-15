number= int(input("Enter a non-negative integer: "))

while number<0:
    print("Enter a non-negative integer.")
    number=int(input("Enter a number: "))

while number>=0:
    print(number)
    number=number-1