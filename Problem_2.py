#Reviewing python by using it to complete Project Euler problems
#Project Euler site: https://projecteuler.net/

#Problem ID: 2

fibSeq = [1,2]

def generateFibonacci():
    counter = 1
    while (fibSeq[counter] < 4000000):
        nextNum = fibSeq[counter] + fibSeq[counter - 1]
        fibSeq.append(nextNum)
        counter = counter + 1

def calculateSum():
    sum = 0
    for i in range(0,len(fibSeq)):
        if (fibSeq[i]%2 == 0):
            sum = sum + fibSeq[i]
    print(sum)

generateFibonacci()
calculateSum()

            
    
