class Solution {
    public int firstStableIndex(int[] nums, int z) {
        if(nums.length==1)  return 0;
        for(int i=0;i<nums.length;i++){
            int max=0;
            double min=Math.pow(10,9);
            int[] ma=Arrays.copyOfRange(nums,0,i+1);
            int[] mi=Arrays.copyOfRange(nums,i,nums.length);
            for(int j=0;j<ma.length;j++){
                if(ma[j]>max)   max=ma[j];
            }
            for(int k=0;k<mi.length;k++){
                if(mi[k]<min)   min=mi[k];
            }
            if((max-min)<=z){
                return i;
            }
        }    
        return -1;
    }
}