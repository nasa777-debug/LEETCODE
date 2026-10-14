class Solution {
    public void moveZeroes(int[] nums) {
        int temp=0;
        int nz=0;
        int z=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0)  z++;
            else if(nums[i]!=0) nz++;
        }
        int[] nza=new int[nz];
        int[] za=new int[z];
        int nzi=0;
        int zi=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
                za[zi++]=nums[i];
            }
            else if(nums[i]!=0){
                nza[nzi++]=nums[i];
            }
        }
        zi=0;
        int k=0;
        for(k=0;k<nza.length;k++){
            nums[k]=nza[k];
        }
        for(int i=0;i<za.length;i++){
            nums[k++]=za[i];
        }
    }
}