import java.util.*;
public class HitCounter {

    Queue<Integer> timestampQ;

    public HitCounter(){
        timestampQ = new LinkedList<>();
        hits  = new LinkedList<>();

    }
    public void hit(int timestamp)
    {
        timestampQ.offer(timestamp);

    }
    public int getHits(int timestamp){
        int size = 0;
        while(!timestampQ.isEmpty() && timestampQ.peekFirst()<=timestamp-300)
            timestampQ.poll();
        return timestampQ.size();
    }

    public static void main(String[] args) {

    }

}
