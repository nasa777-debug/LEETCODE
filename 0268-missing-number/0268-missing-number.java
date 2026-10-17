class Solution {
    public int missingNumber(int[] nums) {
        for(int i=0;i<=nums.length;i++){
            boolean match=false;
            for(int j=0;j<nums.length;j++){
                if(nums[j]==i){
                    match=true;
                    break;
                }
            }
            if(match==false)    return i;
        }
        return -1;
    }
}