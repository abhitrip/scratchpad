import java.util.*;
public class testHeap{
    public static void main(String[] args) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i=0;i<10;i++)
            pq.offer(i);
        Iterator<Integer> it = pq.iterator();
        while(it.hasNext())
            System.out.println(it.next());
    }
}
