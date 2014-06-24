#include <iostream>
#include <cstring>
using namespace std;
bool uniqueString( char* inputString);

int main (int argc, char* argv[]){
	switch (argc){
		case 0:
		case 1: break;
		default:
			cout<<uniqueString(argv[1])<<endl;
	}

	return 0;
}


bool uniqueString (char* inputString){
	int charFlagMap[256]={};
	int i;
	int j;
	for (i=0; i< strlen(inputString); i++){

		charFlagMap[(int)inputString[i]]++;
	} 
	for (int k =0; k<256; k++){
	}

	for(j=0; j<256; j++){
		if (charFlagMap[j]>1){
			return false;
		}
	}
	return true;
}
