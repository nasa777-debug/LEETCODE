class Solution {
    public boolean isPerfectSquare(int num) {
        long left=1;
        long right=num;
        long mid=0;
        long square=1;
        while(left<=right){
            mid=left+((right-left)/2);
            square=mid*mid;
            if(square==num) return true;
            else if(square<num) left=mid+1;
            else    right=mid-1; 
        }
        return false;
    }
}