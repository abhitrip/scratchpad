import java.lang.*;
import java.util.*;
public class removeDupChar{
    public int findLastIndex(Map<Character,Integer> idxMap){
        if(idxMap.size()==0)
            return -1;
        int minIdx = Integer.MAX_VALUE;
        for(char ch:idxMap.keySet())
        {
            minIdx = Math.min(minIdx,idxMap.get(ch));
        }
        return minIdx;
    }
    public String removeDuplicateLetters(String s){
        if(s==null||s.length()<2)
            return s;
        Map<Character,Integer> idxMap = new HashMap<>();
        for(int i=0;i<s.length();i++)
        {
            idxMap.put(s.charAt(i), i);
        }

        char[] result = new char[idxMap.size()];
        int beg=0,end=0;
        for(int j=0;j<result.length;j++)
        {
            char minChar = 'z'+1;
            end=findLastIndex(idxMap);
            for(int k=beg;k<=end;k++)
            {
                if(idxMap.containsKey(s.charAt(k)) && s.charAt(k)<minChar)
                {
                    minChar = s.charAt(k);
                    beg = k+1;
                }
            }
            System.out.println(minChar);
            result[j] = minChar;
            idxMap.remove(minChar);


        }

        return new String(result);
    }

    public static void main(String[] args) {
        String s = "cbacdcbc";
        removeDupChar obj = new removeDupChar();
        System.out.println(obj.removeDuplicateLetters(s));
    }
}
