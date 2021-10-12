#Print factorail of a number
def fact(n):
    if(n<=1): # if the value is less than 1 or equal 1 return 1
        return 1
    else:
        return n*fact(n-1) #Recall recursively
f=input('Please enter a number \t')
print('Factorial of\t',f,'is \t :',fact(int(f)))