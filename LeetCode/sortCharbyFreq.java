import java.util.*;
public class sortCharbyFreq {
    private static class ValueComparator<K,V extends Comparable<V>> implements Comparator<K> {
        Map<K,V> map;
        public ValueComparator(Map<K,V> map){
            this.map = map;
        }
        @Override
        public int compare(K key1,K key2)
        {
            Comparable<V> value2 = map.get(key2);
            V value1 = map.get(key1);
            return value2.compareTo(value1);
        }
    }
    public static<K,V extends Comparable<V>> Map<K,V> sortByValue(Map<K,V> unsortedMap){
        Map<K,V> sortedMap = new TreeMap<K,V>(new ValueComparator(unsortedMap));
        sortedMap.putAll(unsortedMap);
        return sortedMap;
    }
    public static String frequencySort(String s)
    {
        Map<Character,Integer> count = new HashMap<>();
        char[] res = new char[s.length()];
        for(int i=0;i<s.length();i++)
        {
            int cnt = count.getOrDefault(s.charAt(i),0);
            count.put(s.charAt(i),cnt+1);


        }
        Map<Character,Integer> sortedCnt = sortByValue(count);
        int i=0;
        while(i<s.length())
        {
            for(char c:sortedCnt.keySet())
            {
                int num = sortedCnt.get(c);
                while(num>0 && i<s.length())
                    res[i++] = c;

            }
        }
        return new String(res);
    }
    public static void main(String[] args) {
        String input = "tree";

        System.out.println(frequencySort(input));
    }

}
