def reverseInt(n):
	reverse=0
	while(n>0):
		reverse=reverse*10 + n%10
		n=n//10

	return reverse
number=int(input("Please enter a number you want to reverse "))
print(reverseInt(number))
