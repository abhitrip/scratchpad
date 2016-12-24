import java.text.*;
import java.util.*;
import java.lang.*;

class stringExps  {
    public static void main(String[] args)
    {
        String str = "Sep 17, 2013";
        Date date = new Date(1119280000000L);
        DateFormat df =  DateFormat.getDateInstance(DateFormat.LONG, Locale.GERMANY);
        System.out.println(df.format(date));
    }
}
