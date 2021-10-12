def perfectSum(num):
	sum = 0
	for i in range (1,num ):
		if ( num% i == 0):
			sum = sum + i
	if (num * 2 == sum):
		print ("perfect num" )
	else:
		print ( 'Not a perfect Numbers' )


number = int ( input ( "please enter a number\t" ) )
perfectSum ( number )
