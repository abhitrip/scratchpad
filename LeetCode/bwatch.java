public class Solution {
    public List<String> readBinaryWatch(int num) {

        List<String> res = new ArrayList<>();
        int currTime = 0;
        int start = 0;
        backtrack(res,num,start,currTime);
        return res;
    }
    public void backtrack(List<String> res,int num,int start,int time)
    {
        if(num==0)
        {

            int hours = time>>6;

            int min = time%64;

            if (min < 60 && hours < 12) {
                res.add(String.format("%d:%02d", hours, min));
                }
            return;

        }

        for(int i=start;i<10;i++)
        {
            backtrack(res,num-1,i+1,time|(1<<i));
        }


    }
}
