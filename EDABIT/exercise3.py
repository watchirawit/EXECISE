score = input("Enter Score Grade:")
score = int(score)
if score < 60:
        print ("Your grade is F")
elif score <= 69:
        print ("Your grade is D")
elif score <= 79:
        print ("Your grade is C")
elif score <= 89:
        print ("Your grade is B")
elif score <=100:
        print ("Your grade is A") 
else:
        print ("wrong score")