#rows = int(input('Enter your row: '))
#columns = int(input('Enter your columns: '))
#go_to = int(input('g: '))
#colam = int(input('c: '))
x = y = 0

for row in range(1,21):
    print('',end='')
    print('|',end=' ')
    for column in range(1,6):
        y = x + column
        print(end=' ')
        if y < 10:
            print(end=' ')
        print(y,end=' ')
    x = y 
    if y == 100:
        print('|')
    else:
        print(' |')

