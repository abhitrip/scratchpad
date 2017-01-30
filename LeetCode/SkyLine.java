import java.util.*;
public class Solution {
    public List<int[]> getSkyline(int[][] buildings) {
        List<int[]> res = new ArrayList<>();
        List<int[]> heightMap = new ArrayList<>();
        for(int[] b :buildings)
        {
            heightMap.add(new int[]{b[0],-b[2]}); // Start
            heightMap.add(new int[]{b[1],b[2]}); // End
            
        }
        
        Collections.sort(heightMap,new Comparator<int[]>(){
           @Override
           public int compare(int[] p, int[] q)
           {
               if (p[0]!=q[0])
                   return p[0]-q[0];
               return p[1]-q[1];
           }
        });
        
        //PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        TreeMap<Integer,Integer> maxHeap = new TreeMap<>();
        //maxHeap.offer(0);
        maxHeap.put(0,1);
        int prev=0,curr=-1;
        for(int[] height:heightMap)
        {
            if(height[1]<0)
                maxHeap.put(-height[1],maxHeap.getOrDefault(-height[1],0)+1); // add if start point
            else{
                maxHeap.put(height[1],maxHeap.getOrDefault(height[1],0)-1); // remove if start point
                if (maxHeap.get(height[1])==0)
                    maxHeap.remove(height[1]);
            }
            //curr = maxHeap.peek();
            curr = maxHeap.lastKey();
            if(curr!=prev)
            {
                res.add(new int[]{height[0],curr});
                prev = curr;
                
            }
            
            
        }
        
        
        return res;
        
        
    }
}