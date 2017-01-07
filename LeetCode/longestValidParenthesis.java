public class longestValidParentheses {
    public int longestValidParentheses(String s) {
        if(s.length()<2)
            return 0;
        int [] dp = new int[s.length()];
        int curMax=0;
        for(int i=1;i<s.length();i++)
        {
            if(s.charAt(i)==')'){
                 if(s.charAt(i-1)=='(')
                    {
                        if(i>2)
                            dp[i]=dp[i-2]+2;
                        else
                            dp[i]=2;
                    }
                else if(s.charAt(i-1)==')')
                {

                    if(i-dp[i-1]-1>=0 && s.charAt(i-dp[i-1]-1)=='(')
                    {
                        if(i-dp[i-1]-2>=0)
                            dp[i] = dp[i-1]+2+ dp[i-dp[i-1]-2];
                        else
                            dp[i] = dp[i-1]+2;
                    }

            }
            }
            curMax = Math.max(dp[i],curMax);

        }
        return curMax;
    }
}
