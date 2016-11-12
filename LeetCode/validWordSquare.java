import java.util.*;
import java.lang.*;
public class ValidWordSquare {
    public List<String>sentence;
    public ValidWordSquare(String[] seqs){
        sentence = new ArrayList<>();
        for(int i=0;i<seqs.length;i++)
            sentence.add(seqs[i]);
    }
    public boolean validWordSquare(List<String> words)
    {
         int i=0;
            int len = words.size();
            for(i=0;i<len;i++)
            {
                int limit = words.get(i).length();
                for(int j=0;j<limit;j++)
                {
                    if(j>=len ||words.get(j).length()<=i|| words.get(i).charAt(j)!=words.get(j).charAt(i))
                        return false;
                }
            }

            return true;
    }


}
