import java.util.*;
import java.lang.*;
public class permutations {

    public static void backtrack(List<Character> tmp,List<String> res,int start,char[] s)
    {
        if(start==s.length)
        {
            res.add(new String(s));
            return;
        }
        for(int i=start;i<s.length;i++)
        {
            s[i] = Character.toUpperCase(s[i]);
            backtrack(tmp,res,start+1,s);
            s[i] = Character.toLowerCase(s[i]);

        }

    }

    public static void main(String[] args) {
        char[] str = {'a','b','c'};
        List<Character> tmp = new ArrayList<>();
        List<String> res = new ArrayList<>();
        backtrack(tmp,res,0,str);
        for(String s:res)
            System.out.println(s);
    }
}
