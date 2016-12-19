public class yelp  {

    public String removeDupE(String input)
    {
        StringBuilder sb = new StringBuilder();
        int i=0,j=1;
        int len = input.length();
        while(i<len && j<len)
        {
            if(input.charAt(i)!='e')
            {
                sb.append(input.charAt(i));
                i++;
            }
            else
            {
                j = i+1;
                while(j<len && input.charAt(j)=='e')
                    j++;
                sb.append('e');
                i = j;
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        String test = "abceeeeed";
        yelp obj = new yelp();
        System.out.println(obj.removeDupE(test));
    }

}
