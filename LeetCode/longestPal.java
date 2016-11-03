public class Solution {
    public String longestPalindrome(String s) {

        if(s.length()<2)
            return s;
        int maxLen = Integer.MIN_VALUE;
        String longest="";
        int i=0;
        while(i<s.length()-1)
        {
            String curr = helper(s,i,i);
            if(curr.length()>maxLen)
            {
                maxLen = curr.length();
                longest = curr;
            }
            curr = helper(s,i,i+1);
            if(curr.length()>maxLen)
            {
                maxLen = curr.length();
                longest = curr;
            }
            i++;

        }
        return longest;
    }
    public String helper(String s,int beg,int end)
    {
        while(beg>=0 && end <s.length() && s.charAt(beg)==s.charAt(end))
        {
            beg--;
            end++;
        }
        return s.substring(beg+1,end);

    }
}
