import java.util.*;
public class countAndSay {

    public String countAndSayHelper(String n) {
        String num = n;
        int i = 0;int j=0;
        String res="";
        while(i<num.length())
        {
            j=i;
            while(j<num.length() && num.charAt(j)==num.charAt(i))
            {
                j++;
            }
            res += String.valueOf(j-i)+(num.charAt(i)-'0');
            //System.out.println(res);
            i = j;
        }
        return res;
    }

    public String countAndSay(int n)
    {
        int i=1;
        if(n==i)
            return "1";

        int intRes = 1;
        String strRes="1";
        while(i<n)
        {
            strRes = countAndSayHelper(strRes);

            i++;
        }
        return strRes;
    }

    public static void main(String[] args) {
        int n=9;
        System.out.println(countAndSay(n));

    }

}
