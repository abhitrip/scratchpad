import java.util.*;
import java.lang.*;
class TrieNode {
    Map<Character,TrieNode> children;
    boolean endOfWord;
    public TrieNode(){
        children = new HasMap<>();
        endOfWord = false;
    }
}
public class Trie{
    private final TrieNode root;
    public Trie(){
        root = new TrieNode();
    }
    // Inserting a word into a trie
    public void insert(String word){
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
    public boolean search(String word){
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
    public boolean startsWith(String prefix){
        TrieNode curr = root;
        for(int i=0;i<prefix.length();i++)
        {
            char ch = prefix.charAt(i);
            TrieNode node = curr.children.getOrDefault(ch,null);
            if(node==null)
                return false;
            curr = node;
        }
        return true;
    }

}
