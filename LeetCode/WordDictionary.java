public class WordDictionary {

    // Adds a word into the data structure.

    private class TrieNode{
        Map<Character,TrieNode> children;
        boolean endOfWord;
        public TrieNode(){
            children = new HashMap<>();
        }
    }

    private TrieNode root;
    public WordDictionary(){
        root = new TrieNode();
    }

    public void addWord(String word) {
         int i=0;
        TrieNode curr = root;
        for(;i<word.length();i++)
        {
            char ch = word.charAt(i);
            TrieNode child = curr.children.getOrDefault(ch,null);
            if(child==null)
            {
                child = new TrieNode();
                curr.children.put(ch,child);
            }
            curr = child;
        }
        curr.endOfWord = true;
    }
    public boolean dfs(String word,int pos,TrieNode root){
        if(pos==word.length())
        {
            return root.endOfWord;
        }
        char ch = word.charAt(pos);
        if(ch=='.')
        {
            for(char c:root.children.keySet()){
                TrieNode node = root.children.getOrDefault(c,null);
                if(node!=null && dfs(word,pos+1,node))
                    return true;
            }

        }
        else if(root.children.getOrDefault(ch,null)!=null){

            TrieNode node = root.children.get(ch);
            return dfs(word,pos+1,node);

        }
        return false;
    }
    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) {
         TrieNode curr = root;
        return dfs(word,0,curr);

    }
}

// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary = new WordDictionary();
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");
