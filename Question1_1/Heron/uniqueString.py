#!/usr/bin/env python
import sys

def main():
	print	"Unique String?: " + str(uniqueString(str(sys.argv[1])))

def uniqueString(tempString):
	print tempString
	newString ="".join( sorted(tempString))
	print newString
	for a in range(len(newString)-1):
#		print newString[a] + " &" +newString[a+1]
		if (newString[a] == newString[a+1]):
#			print "duplicate"
			return False
	return True
main()
