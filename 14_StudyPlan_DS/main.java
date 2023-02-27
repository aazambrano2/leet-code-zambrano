import java.util.*;
public class main {
    public static boolean containsDuplicate(int[] nums) {
        if (nums.length <= 1){
            return false;
        }
        Set<Integer> mySet = new HashSet<Integer>();

        for(int i=0; i < nums.length; i++){
            if(mySet.contains(nums[i])){
                return true;
            }
            else{
                mySet.add(nums[i]);
            }
        }
        return false;
    }

    public static int maxSubArray(int[] nums) {

        // if(nums.length == 1){
        //     return nums[0];
        // }

        // if(nums.length == 0 ||nums == null){
        //     return 0;
        // }

        // //'current' sum to compare with subArrays
        // int sum = 0;
        // for (int value : nums) {
        //     sum += value;
        // }
        
        // //prepare for next subarray to check.
        // //Since this array is primative, we must copy to a new array...increasing space complexity :(
        // //At least...this is as far as I know
        // //-1 elements from beginning and end
        
        // // int[] subArrayM = new int[nums.length-2]; take account something in the middle?
        // int[] subArrayL = new int[nums.length-1];
        // int[] subArrayR = new int[nums.length-1];

        // // for(int i=0; i<subArrayM.length;i++){
        // //      subArrayM[i] = nums[i+1];
        // // }

        // for(int i=0; i<subArrayL.length;i++){
        //      subArrayL[i] = nums[i];
        // }

        // for(int i=0; i<subArrayR.length;i++){
        //     subArrayR[i] = nums[i+1];
        // }
        // //recursively send subArray to check.

        // return Math.max(sum,Math.max(maxSubArray(subArrayL),maxSubArray(subArrayR)));

        //^^^above solution is 197/210 but the Time Limit get Exceeded because of the time complexity as well as the space complexity

        //Below os a linear solution

        //by abstractConnoisseurs
        int curSum = nums[0];
        int maxSum = nums[0];
        for(int i = 1; i < nums.length; i++) {
            if(curSum < 0) {
                curSum = 0;
            }
            curSum += nums[i];
            maxSum = Math.max(maxSum, curSum);
        }
        return maxSum;
    }


    public static void main(String[] args) {
        int[] array = { 1,1,1,3,3,4,3,2,4,2};
        boolean answer = containsDuplicate(array);
        System.out.println(answer);

        int[] array2 = {-2,1,-3,4,-1,2,1,-5,4};
        int answer_max = maxSubArray(array2);
        System.out.println(answer_max);
    }
    
}
