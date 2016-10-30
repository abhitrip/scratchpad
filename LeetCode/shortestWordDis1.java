public class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        int w1=-1,w2=-1;
        int minDiff = Integer.MAX_VALUE;
        boolean flag1=false,flag2=false;
        for(int i=0;i<words.length;i++)
        {
            String currWord = words[i];
            if(currWord.equals(word1))
               {
                   flag1 = true;
                   w1 = i;
               }
            if(currWord.equals(word2))
            {
                flag2 = true;
                w2 = i;
            }
            if(flag1 && flag2)
                minDiff = Math.min(minDiff,Math.abs(w1-w2));
            
                
        }
        return minDiff;
        
    }
}