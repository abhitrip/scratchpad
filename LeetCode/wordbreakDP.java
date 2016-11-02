public class wordbreakDP {
    String s,
    Set<String> dict;
    public wordbreakDP(String s,Set<String>Dict){
        this.s = s;
        this.dict = Dict;
    }
    public boolean wordBreak(String s, Set<String> wordDict){
        boolean[] pos = new boolean[s.length()+1];
        pos[0] = true;

        for(int i=0;i<s.length();i++)
        {
            if(!pos[i])
                continue;
            for(String word:wordDict)
            {
                int start = i;
                int end = i +word.length();
                if(end>s.length())
                    continue;
                String subs = s.substring(start,end);
                if(t[end])
                    continue;
                if(subs.equal(word))
                    t[end] = true;
            }
        }
        return t[s.length()];
    }
}
