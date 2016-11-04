public class Solution {
    public int lengthLongestPath(String input) {
        String[] res = input.split("\\n");
        Stack<Integer> parLen = new Stack<>();
        int maxLen = 0;
        for(int i=0;i<res.length;i++)
        {
            int lev = 0;
            int len = res[i].length();
            while(res[i].charAt(lev)=='\t') lev++;
            

            len = len - lev;
            while(parLen.size()>lev)
                parLen.pop();
                
            if(!parLen.isEmpty())
                len = parLen.peek()+1+len;
            
            if(res[i].indexOf('.')==-1)
                parLen.push(len);
            
            else
                maxLen = Math.max(len,maxLen);
            
           
            
        }
        
        return maxLen;
    }
}