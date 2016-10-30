public class WordDistance {
    Map<String,List<Integer>> map;
    public WordDistance(String[] words) {
        int i=0;
        map = new HashMap<>();
        for(;i<words.length;i++)
        {
            String word_i = words[i];
            List<Integer> pos = map.getOrDefault(word_i,new ArrayList<>());
            pos.add(i);
            map.put(word_i,pos);
        }
    }

    public int shortest(String word1, String word2) {
        int i=0,j=0;
        List<Integer> arr1 = map.get(word1);
        List<Integer>arr2 = map.get(word2);
        int minDiff =Integer.MAX_VALUE;
        while(i<arr1.size() && j<arr2.size())
        {
            minDiff = Math.min(minDiff,Math.abs(arr1.get(i) - arr2.get(j)));
            if(arr1.get(i)>arr2.get(j))
                {

                        j++;

                }
            else
                i++;

        }
        return minDiff;
    }
}
