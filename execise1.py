score1 = int(input('enter the score for test1:  '))
score2 = int(input('enter the score for test2:  '))
score3 = int(input('enter the score for test3:  '))
score_all = (score1 + score2 + score3) / 3 
if score_all >= 95 : 
    print("the average score is",score_all,"\ncongratulations!\nthat is a great average")  
    
if score_all < 95 :
    print("the average score is",score_all)
 