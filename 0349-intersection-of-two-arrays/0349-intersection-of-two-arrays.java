class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashMap<Integer,Integer> h1=new HashMap<>();
        HashMap<Integer,Integer> h2=new HashMap<>();
        for(int i=0;i<nums1.length;i++){
            if(h1.containsKey(nums1[i]))    continue;
            h1.put(nums1[i],i);
        }
        for(int i=0;i<nums2.length;i++){
            if(h2.containsKey(nums2[i]))    continue;
            h2.put(nums2[i],i);
        }
        ArrayList<Integer> a=new ArrayList<>();
        for(int i:nums1){
            if(a.contains(i))   continue;
            if((h1.containsKey(i))&&(h2.containsKey(i))){
                a.add(i);
            }
        }
        int[] res=new int[a.size()];
        int k=0;
        for(Integer i:a){
            res[k++]=i;
        }
        return res;
    }
}