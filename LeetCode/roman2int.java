public class Solution {
    public int romanToInt(String s) {
        Map<Character,Integer> map = new HashMap<>();
        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);
        int i=0;
        int res=0;
        while(i<s.length()-1)
        {
            if(map.get(s.charAt(i+1))>map.get(s.charAt(i)))
                res -= map.get(s.charAt(i));
            else
                res += map.get(s.charAt(i));


            i++;
        }
        res+= map.get(s.charAt(i));
        return res;
    }
}