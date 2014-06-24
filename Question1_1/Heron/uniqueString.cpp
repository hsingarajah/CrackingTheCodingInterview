#include <iostream>
#include <algorithm>

using namespace std;
bool uniqueString( string inputString);
bool uniqueString2(string inputString);


int main (int argc, char* argv[]){
	switch (argc){
		case 0:
		case 1: break;
		default:
			cout<<"unique string "<<uniqueString(argv[1])<<endl;
			cout<<"unique string2 "<<uniqueString2(argv[1])<<endl;
	}

	return 0;
}


bool uniqueString (string inputString){
	/*create a table to count all occurances of each character*/
	int charFlagMap[256]={};

	/*for each character in the string, find the value of that character and increment the count table*/
	for (int i=0; i< inputString.length(); i++){

		charFlagMap[(int)inputString[i]]++;
	} 

	/*for every character in the map, check if any character count is greater than 1. if so it's not unique so return false*/
	for(int j=0; j<256; j++){
		if (charFlagMap[j]>1){
			return false;
		}
	}
	/*if sucessfully checked every element and any character is found 0 or 1 times,then return true*/
	return true;
}

bool uniqueString2(string inputString){

	/*sort all characters in string so that characters of the same value are beside each other*/
	sort(inputString.begin(), inputString.end());

	/*for all characters in the string, check if any two adjacent characters are equal. If so they're not unique so exit false*/
	for (int i=0; i<inputString.length()-1; i++){	
		if (inputString[i]==inputString[i+1]){
			return false;		
		}
	}
	/*if the entire string is iterated and not exited, no two adjacent values are equal so all characters are unique*/
	return true;
}
