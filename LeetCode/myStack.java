import java.util.*;
public class myStack {
    Queue<Integer> q1 = new LinkedList<>();
    Queue<Integer> q2 = new LinkedList<>();
    int top;
    public void push(int x)
    {
        top = x;
        if(!q1.isEmpty())
        {
            q1.add(x);
        }
        else
        {
            q2.add(x);
        }


    }
    public int pop()
    {
        if(empty())
            return -Integer.MIN_VALUE;
        if(!q1.isEmpty())
        {
            while(q1.size()>1)
            {
                top = q1.remove();
                q2.add(top);

            }
            System.out.println(q2);
            return q1.remove();
        }
        while(q2.size()>1)
            {
                top = q2.remove();
                q1.add(top);
            }
            return q2.remove();
    }
    public boolean empty()
    {
        return (q1.size()==0 && q2.size()==0);
    }
    public int top()
    {
        if(!empty())
        {
            return top;
        }

        return Integer.MIN_VALUE;
    }
    public static void main(String[] args) {
        myStack obj = new myStack();
        obj.push(1);
        obj.push(2);
        obj.push(3);
        System.out.println(obj.top());
        System.out.println(obj.pop());
        System.out.println(obj.top());
    }

}
