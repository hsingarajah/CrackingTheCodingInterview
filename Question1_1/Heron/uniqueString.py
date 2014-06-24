#!/usr/bin/env python
import sys

def main():
	if (len(sys.argv)>1):
		print	"Unique String?: " + str(uniqueString(str(sys.argv[1])))
		print	"Unique String2?: " + str(uniqueString2(str(sys.argv[1])))


def uniqueString(tempString):

	#create a sorted version of the string. using "".join ensures that the list is converted into a string
	newString ="".join( sorted(tempString))

	# for every character in the string, check if its adjacent character is equal. if so it is not unique so return false
	for a in range(len(newString)-1):
		if (newString[a] == newString[a+1]):
			return False
	# if every character is checked, then all values are unique so return true
	return True

def uniqueString2(tempString):
	#integer array, by type code 'i'
	charMap=[0]*256

	#for every character in string, find its integer value in the charMap array and increment the count
	for a in tempString:
		charMap[ord(a)]+=1

	#go through character map and find any chars that are greater than 1. if so, it's not unique so return false
	for a in charMap:
		if (a>1):
			return False
	#otherwise, if all elements are 1 or less, return true
	return True

####################
main()
