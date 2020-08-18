keep_going = 'y' 
while keep_going == 'y' or keep_going == "Y":
    wholesale = float(input("Enter the item's wholesale cost: "))
    
    print('retail price: $' , \
        format(wholesale*2.5,',.2f'), sep='')
    keep_going = input('do you have another item? (Enter y for yes):')
             