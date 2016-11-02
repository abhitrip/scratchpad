public class Solution {
    class Pair{
        String s;
        int level;
        public Pair(String _s,int _level)
        {
            s = _s;
            level = _level;
        }
    }
    public  String compose(int rep,int chid,String s)
    {
        char[] ch = s.toCharArray();
        ch[rep] = (char)('a'+chid);

        return new String(ch);
    }
    public  int ladderLength(String beginWord, String endWord, Set<String> wordList) {
           int i=0;
           Queue<Pair> bfsq = new LinkedList();
           bfsq.offer(new Pair(beginWord,1));
           Set<String>words = new HashSet<>();
           words.add(beginWord);
           int len = beginWord.length();

           while(!bfsq.isEmpty())
           {
                String curr = bfsq.peek().s;
                int level = bfsq.peek().level;
                bfsq.poll();
                if(curr.equals(endWord))
                    return level;
                for(i=0;i<len;i++)
                {
                    for(int j=0;j<26;j++)
                    {
                        String newStr = compose(i,j,curr);
                        if(!words.contains(newStr)&&wordList.contains(newStr))
                        {
                            bfsq.offer(new Pair(newStr,level+1));
                            words.add(newStr);
                        }
                    }
                }
           }
           return 0;
    }
}
