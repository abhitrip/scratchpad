import java.util.ArrayList;
import java.util.Iterator;
import java.util.*;

public class vector2D implements Iterator<Integer>{
     int x,y;

        List<List<Integer>> data;
        public vector2D(List<List<Integer>> vec2d) {
            data = new ArrayList<>(vec2d);
            x = 0;
            y = 0;
        }

        @Override
        public Integer next() {
            int val =0;
            // For the last element move row to next and col to zero
            if(y==data.get(x).size()-1)
            {
                val = data.get(x).get(y);
                x++;
                y=0;

            }
            // Else just increment column
            else
            {
                val = data.get(x).get(y);
                y++;
            }



             return val;


        }

        @Override
        public boolean hasNext() {
             // Check if vec2d is empty
             if(data.size()==0)
                return false;
            // First Remove zero content rows
            while(x<data.size() && data.get(x).size()==0)
                x++;
            // Check if Everything has traversed
            if(x>=data.size())
                return false;
            // Check if last row and all columns traversed
            else if(x==data.size()-1 && y==data.get(x).size())
                return false;
            return true; // For all other cases vec2D.next() exists

        }
    }
