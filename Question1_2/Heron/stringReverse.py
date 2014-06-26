#!/usr/bin/env python
import sys
def stringReverse(tempString):

	#create a list of each character
	a=list(tempString)
	#go to half way point of string, and swap increaseing index from 0 to decreasing index from last
	for index in range(0,len(a)/2):
		temp=a[index]
		a[index]=a[(len(a)-1)-index]
		a[ (len(a)-1)-index]=temp
	#return string
	return "".join(a)

#python is awesome, includes a reverse list
def stringReverseHaHaPython(tempString):
	a=list(tempString)
	a.reverse()
	return "".join(a)

def main():
	if (len(sys.argv)>1):
		print	"Reverse of: " + str(sys.argv[1])+"\t "+ str(stringReverse(str(sys.argv[1])))
		print	"Reverse of: " +str(sys.argv[1])+"\t "+str(stringReverseHaHaPython(str(sys.argv[1])))

main()
