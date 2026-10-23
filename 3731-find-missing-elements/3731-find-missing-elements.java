class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        Arrays.sort(nums);
        int min=nums[0];
        int max=nums[nums.length-1];
        int[] newarr=new int[max-min+1];
        int k=0;
        for(int i=min;i<=max;i++){
            newarr[k++]=i;
        }
        List<Integer> l=new ArrayList<Integer>();
        for(int i=0;i<newarr.length;i++){
            boolean found=false;
            for(int j=0;j<nums.length;j++){
                if(nums[j]==newarr[i]){
                    found=true;
                }
            }
            if(found==false)    l.add(newarr[i]);
        }
        return l;
    }
}