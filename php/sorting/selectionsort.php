<?php 

$arr = [64,25,12,22,11];

$count = count($arr)-1;
for($i=0;$i<$count;$i++){
    for($j=0;$j<$count;$j++){
        if($arr[$j]>$arr[$j+1]){
            $t = $arr[$j];
            $arr[$j] = $arr[$j+1];
            $arr[$j+1]=$t;
        }   
    }
}

print_r($arr);