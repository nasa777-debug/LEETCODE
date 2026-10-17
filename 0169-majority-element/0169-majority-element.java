class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> h=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(h.containsKey(nums[i]))  h.put(nums[i],h.get(nums[i])+1);
            else    h.put(nums[i],1);
        }
        int c=0;
        for(Integer i:h.values()){
            if(c<i) c=i;
        }
        for(Integer i:h.keySet()){
            if(h.get(i)==c) return i;
        }
        return 0;
    }
}