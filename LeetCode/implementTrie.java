class TrieNode {
    // Initialize your data structure here.
    Map<Character,TrieNode> children;
    boolean endOfWord;

    public TrieNode() {
            children = new HashMap<>();
            endOfWord = false;
        }
}

public class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        TrieNode curr = root;
        char ch='0';
        for(int i=0;i<word.length();i++)
        {
            ch = word.charAt(i);
            TrieNode child = curr.children.getOrDefault(ch,null);
            if(child==null)// Creating Children when
            {
                child = new TrieNode();
                curr.children.put(ch,child);
            }
            curr = child;
        }
        // This denotes end of word
        curr.endOfWord = true;
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
        TrieNode curr = root;
        for(int i=0;i<word.length();i++)
        {
            char ch = word.charAt(i);
            TrieNode node = curr.children.getOrDefault(ch,null);
            if(node==null)
                return false;
            curr = node;
        }
        return curr.endOfWord;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
        TrieNode curr = root;
        for(int i=0;i<prefix.length();i++)
        {
            char ch = prefix.charAt(i);
            TrieNode node = curr.children.getOrDefault(ch,null);
            if(node==null)
                return false;
            curr = node;
        }
        return curr!=null;
    }

}

// Your Trie object will be instantiated and called as such:
// Trie trie = new Trie();
// trie.insert("somestring");
// trie.search("key");
