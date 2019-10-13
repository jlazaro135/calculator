print ("INSTRUCTIONS OF THE CALCULATOR: First, you have to write the first number and then the second one. Afterwards, you have to choose what kind of operation you want to made.")

first_number = int(input("type first number: "))
print (first_number)

second_number = int(input("type second number: "))
print (second_number)



operation = input ("what kind of operation you want to do: addition, substration, multiplication or division: ?")

if operation == "addition":
    print (first_number + second_number)
elif operation == "substration":
    print (first_number - second_number)
elif operation == "multiplication":
    print (first_number * second_number)
else:
    print (first_number / second_number)

