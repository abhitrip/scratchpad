import java.util.*;
import java.lang.*;
public class validateIP {

    public static void  validate(String ip)
    {
        String[] splitip4 = ip.split("\\.");
        boolean isip4 = true;
        boolean flag = false;
        boolean isip6 = true;
        if(splitip4.length!=4)
            isip4 = false;
        else
        {

            for(String s:splitip4)
            {
                try{
                    int x = Integer.parseInt(s);
                    if(x<0 || x>255)
                    {

                        isip4 = false;
                        flag = true;
                        System.out.println("Im here");
                        break;
                    }
                }
                 catch(NumberFormatException e){
                    flag = true;
                    isip4 = false;

                    break;
                 }

                }
            }


       if(ip.indexOf(':')==-1)
            isip6 = false;
        else{
            String[] splitip6 = ip.toLowerCase().split(":");
            for(String s:splitip6)
            {
                if(s.length()>4)
                    break;
                for(int j=0;j<s.length();j++)
                {
                    if(!Character.isDigit(s.charAt(j))&&(s.charAt(j)<'a' && s.charAt(j)>'f')){

                        isip6 = false;
                        break;
                    }

                }


            }




        }


       if(isip4)
            System.out.println("ip4");
        else if(isip6)
            System.out.println("ip6");
        else
            System.out.println("neither");

    }
    public static void main(String[] args) {
        String ip1="2001:0db8:0000:0000:0000:ff00:0042:8329";
       validate(ip1);
    }

}
