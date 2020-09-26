number=1234
while number>0:
    #get last integer
    digit=number%10
    #remove the last and repeat loop
    number=number//10
    print(digit,end=' ')