#!/usr/bin/env python
import sys
import subprocess
def main():
	#test cases
	testCases={
	"",
	"a",
	"abcd",
	"aabcd",
	"abbcd",
	"abcda",
	"abcddcba",
	"abcdabcd"}
	
	#iterate through all test cases in the array
	for testString in testCases:
		#test input is built as a shell command for php script.
		#php script takes its input string from comand line
		testInput="php remDup.php "+testString
		
		#call shell script from commandline using input from testCases
		proc = subprocess.Popen(testInput, shell=True, stdout=subprocess.PIPE)
		#save output returned from remove duplicate function
		output=(proc.stdout.read()).strip()

		#print test case and returned output. can be logged if necesary
		print "Test Case: " + testString +"_Output: "+output

		#assert all test results
		assert(uniqueString(output))

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
