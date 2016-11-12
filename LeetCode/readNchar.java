/* The read4 API is defined in the parent class Reader4.
      int read4(char[] buf); */

public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    public int read(char[] buf, int n) {

        int res=0;
        char[] tmp = new char[4];
        while(res<n)
        {
            int bytes = read4(tmp);
            System.out.print(bytes);



            for(int i=0;i<bytes;i++)
                buf[res+i] = tmp[i];
            res+=bytes;
            if(bytes<4)
                break;
        }

        return res>n?n:res;

    }
}
