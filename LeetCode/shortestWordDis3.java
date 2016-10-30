public class Solution {
    public int shortestWordDistance(String[] words, String word1, String word2) {
        int i=0;
        int w1=-1,w2=-1;
        int minDiff = Integer.MAX_VALUE;
        int prev = -1;
        for(;i<words.length;i++)
        {
            if(word1.equals(word2) && words[i].equals(word1))
            {
                if(prev!=-1)
                    minDiff = Math.min(i-prev,minDiff);
                prev = i;
            }
            else{
                if(word1.equals(words[i]))
                    w1 = i;
                if(word2.equals(words[i]))
                    w2 = i;
                if(w1!=-1 && w2!=-1)
                    minDiff = Math.min(Math.abs(w1-w2),minDiff);
            }


        }
        return minDiff;
    }
}
