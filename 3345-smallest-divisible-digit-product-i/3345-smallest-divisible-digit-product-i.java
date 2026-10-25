class Solution {
    public int smallestNumber(int n, int t) {
        int res=0;
        for(int i=n;i<n+10;i++){
            int p=1;
            int temp=i;
            while(temp>0){
                p=p*(temp%10);
                temp/=10;
            }
            if(p%t==0){
                res=i;
                break;
            }  
        }
        return res;
    }
}