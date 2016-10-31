import java.util.*;
import java.lang.*;
public class simplifyPaths {
    public static String simplify(String path){
        Stack<String> pthStk = new Stack<>();
        String[] pathArr = path.split("/");
        for(String s:pathArr)
        {
            if(s.length()==0||s.equals("."))
                continue;
            if(s.equals(".."))
            {
                if(pthStk.size()>=1)
                    pthStk.pop();
            }
            else
                pthStk.push(s+"/");

        }

        String resPath= "";
        while(!pthStk.isEmpty())
        {
            resPath=pthStk.pop()+resPath;
        }
        resPath = "/"+resPath;
        if(resPath.length()>1)
            resPath = resPath.substring(0,resPath.length()-1);
        return resPath;
    }
    public static void main(String[] args) {
        String path="/a/./b/../../c/";
        System.out.println(simplify(path));
    }
}
