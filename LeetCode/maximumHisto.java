import java.util.*;
public class maximumHisto {
    public int largestRectangleArea(int[] height) {
        Stack<Integer> stk = new Stack<>();
        int stkTop;
        int area=0,maxarea=-1;
        int x=0;
        for(x=0;x<height.length;)
        {
            if((stk.isEmpty())||(height[x]>height[stk.peek()]))
                {
                    stk.push(x);x++;
                }
            else{

                    stkTop = stk.pop();
                    if(stk.isEmpty())
                        area = height[stkTop]*x;
                    else{
                        area = (x-stk.peek()-1)*height[stkTop];
                    }

                    maxarea = Math.max(maxarea,area);


                }

            }


        while(!stk.isEmpty())
        {
            stkTop = stk.pop();
            if(stk.isEmpty())
                area = height[stkTop]*x;
            else
                area = height[stkTop]*(x-stk.peek()-1);
            maxarea = Math.max(area,maxarea);
        }
        return maxarea;
    }
    public static void main(String[] args) {
        int histo1[] = new int[]{2,1,5,6,3};
        maximumHisto obj = new maximumHisto();
        System.out.println(obj.largestRectangleArea(histo1));
    }
}
