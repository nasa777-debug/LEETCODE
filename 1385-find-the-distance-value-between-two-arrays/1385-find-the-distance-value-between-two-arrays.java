class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        int c=0;
        for(int i=0;i<arr1.length;i++){
            int d1=0;
            boolean gt2=true;
            for(int j=0;j<arr2.length;j++){
                d1=Math.abs(arr1[i]-arr2[j]);
                if(d1<=d){
                    gt2=false;
                    break;
                }
            }
            if(gt2==true){
                c++;
            }
        }
        return c;
    }
}