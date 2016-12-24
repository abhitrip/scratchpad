public class Solution {
    public void reverseWords(char[] s) {
        int i=0,j=0;
        int nonSpace=0;
        boolean isSingle = true;
        reverse(s,0,s.length-1);
        for(;i<s.length;i++)
        {
            if(s[i]==' ')
                {
                    reverse(s,nonSpace,i-1);
                    nonSpace = i+1;
                    isSingle = false;
                }

        }

        reverse(s,nonSpace,s.length-1);
    }
    public static void reverse(char[] s,int st,int end)
    {
        while(st<end)
        {
            char tmp = s[st];
            s[st] = s[end];
            s[end] = tmp;
            st++;
            end--;
        }
    }
}
