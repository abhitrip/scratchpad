public class Solution {
    private class Point{
        int start;
        int end;
        public Point(int x,int y)
        {
            this.start = x;
            this.end = y;
        }
        
    }
    public int findMinArrowShots(int[][] points) {
        
        if(points.length==0)
            return 0;
        
        
        List<Point> pts = new ArrayList<>();

        
        for(int i=0;i<points.length;i++)
            pts.add(new Point(points[i][0],points[i][1]));
            
        Collections.sort(pts,new Comparator<Point>(){
           @Override
           public int compare(Point x,Point y)
           {
               Integer o1 = x.start;
               Integer o2 = y.start;
               return o1.compareTo(o2);
           }
        });
        
        
        int currEnd = pts.get(0).end;
        int numBaloons = 1;
        for(int i=0;i<pts.size();i++)
        {
            
            
            
            if(currEnd<pts.get(i).start)
            {
                numBaloons++;
                currEnd = pts.get(i).end;
                
            }
            
            else if(currEnd>pts.get(i).end)
            {
                currEnd = pts.get(i).end;
            }
            System.out.println(currEnd);
            
            
        }
        //numBaloons++;
        return numBaloons;
    }
}