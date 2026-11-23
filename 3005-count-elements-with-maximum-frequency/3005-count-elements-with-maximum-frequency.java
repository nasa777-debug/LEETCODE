class Solution {
    public int maxFrequencyElements(int[] nums) {
        int max_freq=0;
        int sum=0;
        HashMap<Integer,Integer> h=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(h.containsKey(nums[i]))  h.put(nums[i],h.get(nums[i])+1);
            else    h.put(nums[i],1);
        }
        for(Integer val:h.values()){
            if(max_freq<val){
                max_freq=val;
            } 
        }
        for(int i=0;i<nums.length;i++){
            if(h.get(nums[i])==max_freq){
                sum++;
            }
        }
        return sum;
    }
}