#Check whether two strings are anagram of each other
# Python program to check whether two strings are
# anagrams of each other

# function to check whether two strings are anagram
# of each other


def areAnagram(str1, str2):
	# Get lengths of both strings
	n1 = len(str1)
	n2 = len(str2)

	# If lenght of both strings is not same, then
	# they cannot be anagram
	if n1 != n2:
		return 0

	# Sort both strings
	str1 = sorted(str1)
	str2 = sorted(str2)

	# Compare sorted strings
	for i in range(0, n1):
		if str1[i] != str2[i]:
			return 0

	return 1



str1 = "test"
str2 = "ttew"

# Function Call
if areAnagram(str1, str2):
	print("The two strings are anagram of each other")
else:
	print("The two strings are not anagram of each other")

# This code is contributed by Bhavya Jain
