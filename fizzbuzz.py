'''
Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number
and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
tips: Python continue only work with for/while loop
'''
def fizzbuzz(n):

    for i in range(n): #if we want to get (0,n) this perfect,if you want to exclude (1,n) set the range
        if i % 3 == 0 and i % 5 == 0:
            print(i, "fizzbuzz")
            continue
        elif i % 3 == 0:
            print("fizz")
            continue
        elif i % 5 == 0:
            print("buzz")
            continue
        print(i)

fizzbuzz(30)