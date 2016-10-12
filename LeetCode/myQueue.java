import java.util.*;
public class myQueue {
    // Push element x to the back of queue.
    Stack<Integer> s1 = new Stack<>();
    Stack<Integer> s2 = new Stack<>();
    public void push(int x) {
        if(!s1.isEmpty())
            s1.push(x);
        else
            s2.push(x);
    }

    // Removes the element from in front of queue.
    public void pop() {
        if(!s1.isEmpty())
        {
            while(s1.size()>1)
                s2.push(s1.pop());
            s1.pop();
             while(!s2.isEmpty())
                s1.push(s2.pop());

        }
        while(s2.size()>1)
                s1.add(s2.pop());
            s2.pop();
         while(!s1.isEmpty())
                s2.push(s1.pop());


    }

    // Get the front element.
    public int peek() {
        int front = 0;
        if(!s1.isEmpty())
            {
                while(!s1.isEmpty())
                {
                    front = s1.pop();
                    s2.push(front);
                }
                while(!s2.isEmpty())
                {

                    s1.push(s2.pop());
                }

            }
        while(!s2.isEmpty())
                {
                    front = s2.pop();
                    s1.push(front);
                }
                while(!s1.isEmpty())
                {

                    s2.push(s1.pop());
                }
        return front;
    }

    // Return whether the queue is empty.
    public boolean empty() {
        return ((s1.size()==0)&&(s2.size()==0));

    }
    public static void main(String[] args) {
        myQueue obj = new myQueue();
        obj.push(1);
        obj.push(2);

        System.out.println(obj.peek());
        obj.pop();
        System.out.println(obj.peek());
    }
}
