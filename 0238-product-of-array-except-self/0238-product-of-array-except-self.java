class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res=new int[nums.length];
        int p=1;
        for(int i=0;i<nums.length;i++){
            p*=nums[i];
        }
        if(p!=0){
            for(int i=0;i<nums.length;i++)  res[i]=p/nums[i];
            return res;
        }
        else{
            for(int i=0;i<nums.length;i++){
                int f=1;
                for(int j=0;j<nums.length;j++){
                    if(i!=j)    f*=nums[j];
                }
                res[i]=f;
            }
            return res;
        }
    }
}