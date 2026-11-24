class Solution {
    public int firstUniqChar(String s) {
        char[] ch=s.toCharArray();
        for(int i=0;i<ch.length;i++){
            boolean match=false;
            for(int j=0;j<ch.length;j++){
                if((i!=j)&&(ch[i]==ch[j])){
                    match=true;
                    break;
                }
            }
            if(match==false)    return i;
        }
        return -1;
   }
}