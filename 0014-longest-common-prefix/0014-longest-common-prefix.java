class Solution {
    public String longestCommonPrefix(String[] strs) {
        if((strs==null)||(strs.length==0))  return "";
        int x=99999;
        for(int i=0;i<strs.length;i++){
            if(x>strs[i].length())    x=strs[i].length();
        }
        StringBuilder sb=new StringBuilder();
        for(int i=0;i<x;i++){
            char c=strs[0].charAt(i);
            for(int j=0;j<strs.length;j++){
                if(strs[j].charAt(i)!=c)    return sb.toString();
            }
            sb.append(c);
        }
        return sb.toString();
    }
}