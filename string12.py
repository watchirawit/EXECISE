inputmsg = 'English = 78 science = 83 math = 68 history = 65 Art = 90 '
sum1 = 0
i = 0
separatewords = inputmsg.split()
for num in separatewords:
    if num.isnumeric():
        sum1 = sum1 + int(num)
        i = i +1
print('sum is',sum1)
print(sum1/i)


