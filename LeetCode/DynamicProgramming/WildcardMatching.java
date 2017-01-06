public class WildcardMatching{
    public boolean isMatch(String s,String p)
    {
        char[] str = s.toCharArray();
        char[] pat = p.toCharArray();

        boolean isFirst=true;
        int widx=0;
        for(int i=0;i<pat.length;i++)
        {
            if (pat[i]=='*')
            {
                if(isFirst)
                    {
                        pat[widx] = '*';
                        widx+=1;
                        isFirst = false;
                    }
            }
            else{
                pat[widx] = pat[i];
                widx+=1;
                isFirst = true;
            }
        }


        boolean dp[][]= new boolean[s.length()+1][widx+1];
        if (pat[0]=='*' && widx>0)
            dp[0][1]=true;
        dp[0][0] = true;

        for(int i=1;i<dp.length;i++)
        {
            for(int j=1;j<dp[0].length;j++)
            {
                if (pat[j-1]=='?'||str[i-1]==pat[j-1])
                    dp[i][j]= dp[i-1][j-1];
                else if(pat[j-1]=='*'){
                    dp[i][j] = dp[i-1][j]||dp[i][j-1];
                }

            }
        } 


        return dp[s.length()][widx];
    }
    public static void main(String[] args) {
        WildcardMatching wm = new WildcardMatching();
        String s = "a";
        String p = "a";
        System.out.println(wm.isMatch(s, p));
    }
}