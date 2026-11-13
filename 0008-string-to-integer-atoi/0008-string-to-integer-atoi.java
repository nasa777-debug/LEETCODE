class Solution {
    public int myAtoi(String s) {
        int i=0,sign=1;
        if(s==null||s.length()==0)    return 0;
        while(i<s.length() &&  s.charAt(i)==' ')    i++;
        if(i==s.length())   return 0;
        char c=s.charAt(i);
        if(c=='-'){
            sign=-1;
            i++;
        }
        else if(c=='+'){
            i++;
        }
        double res=0;
        while(i<s.length() && Character.isDigit(s.charAt(i))){
            res=res*10+(s.charAt(i)-'0');
            i++;
        }
        if(res*sign>Integer.MAX_VALUE)  return Integer.MAX_VALUE;
        else if(res*sign<Integer.MIN_VALUE) return Integer.MIN_VALUE;
        else    return (int)(res*sign);
    }
}