class Solution {
    public int majorityElement(int[] nums) {
        if (nums.length == 0){
            return 0;
        }

        HashMap <Integer,Integer> counter = new HashMap<>();
        for(int i : nums){
            counter.put(i,counter.getOrDefault(i,0) + 1);
        }
        int max_count = Integer.MIN_VALUE;
        int max_element = 0;
        for(int key : counter.keySet()){
            if(counter.get(key) > max_count){
                max_count = counter.get(key);
                max_element = key;
            }
        }
        return max_element;
    }
}