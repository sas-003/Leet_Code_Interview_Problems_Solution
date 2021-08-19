# def twoSums(arr, n, sum):
# 	# Store counts of all elements
# 	# in a dictionary
# 	mydict = dict()
#
# 	# Traverse through all the elements
# 	for i in range(n):
#
# 		# Search if a pair can be
# 		# formed with arr[i]
# 		temp = sum - arr[i]
#
# 		if temp in mydict:
# 			count = mydict[temp]
# 			for j in range(count):
# 				print("(", temp, ", ", arr[i],
# 					  ")", sep="", end='\n')
#
# 		if arr[i] in mydict:
# 			mydict[arr[i]] += 1
# 		else:
# 			mydict[arr[i]] = 1
#
# arr = [ 1, 5, 7, -1, 5 ]
# n = len ( arr )
# sum = 6
#
# twoSums ( arr, n, sum )
#
#
'''
#brute force solution
def bruteForce(num,target):
	for i in range (len(num)):
		for j in range(i+1,(len(num))):
			sum=num[i]+num[j]
			if(sum==target):
				return [i,j]
nums=[1,23,345,56,54,446]
target=500
print(bruteForce(nums,target))
'''
def dict_hash(lst,)


