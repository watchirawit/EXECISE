print("Please select operation -\n1.add\n2.subtract\n3.Multiply\n4.Divide")
select = int(input("select operations form 1,2,3,4 : "))
first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))
add = first_number + second_number
subtract = first_number - second_number
multiply = first_number * second_number
divide = first_number / second_number
if select == 1:
    print(first_number,'+',second_number,"=",add)
elif select == 2:
    print(first_number,"-",second_number,"=",subtract)
elif select == 3:
    print(first_number,'*',second_number,"=",multiply)
elif select == 4:
    print(first_number,"/",second_number,"=",divide)
else:
    print("Please select a new option.")