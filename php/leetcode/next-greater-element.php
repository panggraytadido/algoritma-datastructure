<?php
function nextGreaterElement($nums1, $nums2) {
        $result = []; 
        foreach ($nums1 as $num1Index => $num1) {
            $isHasSameNum = false; 
            foreach ($nums2 as $num2) { 
                if ($num1 === $num2) 
                { 
                    $isHasSameNum = true;
                }
                
                if ($isHasSameNum && $num2 > $num1) { $result[$num1Index] = $num2;
                    break;
                }
            }
            if (!isset($result[$num1Index])) {
                $result[$num1Index] = -1;
            }
        }
        return $result;
    }