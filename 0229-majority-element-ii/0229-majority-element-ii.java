class Solution {
    public List<Integer> majorityElement(int[] nums) {
        HashMap<Integer,Integer> h=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(h.containsKey(nums[i]))  h.put(nums[i],h.get(nums[i])+1);
            else    h.put(nums[i],1);
        }
        ArrayList<Integer> res=new ArrayList<>();
        for(Integer i:h.keySet()){
            if(h.get(i)>(nums.length/3))    res.add(i);
        }
        return res;
    }
}