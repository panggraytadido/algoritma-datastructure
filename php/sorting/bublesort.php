<?php
function sort_arr($arr){
    $count=count($arr);
    for($i=0;$i<$count;$i++){
        for($j=0;$j<$count-$i-1;$j++){
            if ($arr[$j] > $arr[$j+1])
            {
                $t = $arr[$j];
                $arr[$j] = $arr[$j+1];
                $arr[$j+1] = $t;
            }
        }
    }
    return $arr;
}

$arr = [9,8,7,6,5,7,2];
print_r(sort_arr($arr));  