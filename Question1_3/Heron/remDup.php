<?php
#Removes a character from a string given String and index of char
#tempString - the string to modify. Returns a string with a size one less than the original string
#index - the index of the charcter to remove.
function removeChar($tempString,$index){
	$part1 =substr($tempString,0, $index);
	$part2= substr($tempString, $index+1,strlen($tempString));

return $part1 . $part2; 
}

#removes all duplicate values of an input string
function remDup($tempString){
	#calculate the original length of the string
	$initLength = strlen($tempString);
	
	#i represents the reference/unique charcters. As the string is iterated,all duplicates of any character in i will be removed. This maintains the order of the string. 

	for ($i =0; $i < $initLength ; $i++){
		#iterate through the remaining characters of the string, starting with the character ADJACENT to the current reference character
		for ($j =$i+1; $j<$initLength ; $j++){
			#if j is a duplicate of a current reference, then remove it
			if($tempString[$i]==$tempString[$j]){
				$tempString=removeChar($tempString,$j);
				#once the duplicate is removed, update the length of the return string
				$initLength--;
				#reinitialize the inner loop to find more duplicates.
				$j=$i+1;
			}	
		}
	}
return $tempString;

}
if (count($argv)>1){
	echo remDup($argv[1])."\n";
}
?>
