class Solution {
    public boolean isSubsequence(String s, String t) {
        int i=0;
        int j=0;
        if(s.length()==0)   return true;
        char[] s1=s.toCharArray();
        char[] t1=t.toCharArray();
        while(j!=t.length()){
            if(i==s.length())  return true;
            else if(s1[i]==t1[j]){
                i++;
            }
            j++;
        }
        return i==s.length();
    }
}