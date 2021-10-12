'''
Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number
and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
'''
def fizzbuzz(n):

    for i in range(n): #if we want get 0-n ,exclude 0 should be (1,n)
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