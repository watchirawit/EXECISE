print("Please select operation -\n1.add\n2.subtract\n3.Multiply\n4.Divide")
select = int(input("select operations form 1,2,3,4 : "))
first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))
add = first_number + second_number
subtract = first_number - second_number
multiply = first_number * second_number
divide = first_number / second_number
if select == 1:
    print(add)
elif select == 2:
    print(subtract)
elif select == 3:
    print(multiply)
elif select == 4:
    print(divide)
else:
    print("Please select a new option.")