
string = input('enter you string: ')
keep_going = 'y' 
while keep_going == 'y' or keep_going == "Y":
        for i in string:
             if i == 'A' or i == 'C' or i == 'a' or i =='c' or i == 'B' or i == 'b':
                 print('2',end='')
             if i == 'D' or i == 'd' or i == 'F' or i =='f' or i == 'E' or i == 'e':
                 print('3',end='')
             if i == 'H' or i == 'h' or i == 'I' or i =='i' or i == 'G' or i == 'g':
                 print('4',end='')
             if i == 'J' or i == 'j' or i == 'K' or i =='k' or i == 'L' or i == 'l':
                 print('5',end='')
             if i == 'M' or i == 'm' or i == 'N' or i =='n' or i == 'O' or i == 'o':
                 print('6',end='')
             if i == 'P' or i == 'p' or i == 'Q' or i == 'q' or i == 'R' or i == 'r':
                 print('7',end='')
             if i == 'S' or i == 's' or i == 'T' or i =='t' or i == 'U' or i == 'u':
                 print('8',end='')
             if i == 'V' or i == 'v' or i == 'W' or i == 'w' or i == 'X' or i == 'x' or i == 'Y' or i == 'y' or i == 'Z' or i == 'z'  :
                 print('9',end='')
             if i == ' ':
                 print('1',end='')
        keep_going = input('\ndo you have another item? (Enter y for yes):')
        if keep_going == 'y' or keep_going == "Y":
            string = input('enter you string: ')


   
   




