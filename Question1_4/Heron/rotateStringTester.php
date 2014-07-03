<?php
function check_rotation($my_string,$rotation){
	return false;
}

$inputOne=array("","","b", "b","bl", "bl", "blue", "blue", "bluejays","bluejays");
$inputTwo=array("", "hello", "", "b","bl", "lb", "blue", "eblu", "uejaysbl","ejaysbla");
$expectedResult=array(TRUE,FALSE,FALSE,TRUE,TRUE,TRUE,TRUE,TRUE,TRUE,FALSE);

for ($i=0;$i<sizeof($inputOne);$i++){
assert( $expectedResult[$i] == check_rotation($inputOne[$i],$inputTwo[$i]));

}


?>
