// "static void main" must be defined in a public class.
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int arr[] = { 9,8,4,5,6,6 };
        int i, x,count,j,t; 
        count=arr.length;
        for(i=0;i<count;i++){
            for(j=0;j<count-i-1;j++){
                if (arr[j] > arr[j+1])
                {
                    t = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = t;
                }
            }
        }
        
        System.out.println(Arrays.toString(arr));
        //System.out.println(arr);

    }
}