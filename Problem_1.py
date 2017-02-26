#Reviewing python by using it to complete Project Euler problems
#Project Euler site: https://projecteuler.net/

#Problem ID: 1

def multiplesOf3And5 (num):
    sum = 0
    for i in range(1, num):
        if (i%3 == 0) or (i%5 ==0):
            sum = sum + i
    print (sum)

multiplesOf3And5(1000)

            
    
