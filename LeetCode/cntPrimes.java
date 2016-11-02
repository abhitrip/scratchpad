public class Solution {
    public int countPrimes(int n) {
        if(n<2)
            return 0;
        if(n==2)
            return 0;
        boolean[] isPrime = new boolean[n];
        Arrays.fill(isPrime,true);
        isPrime[1] = false;
        isPrime[2] = true;
        for(int j=2;j<Math.sqrt(n);j++)
        {
            if(isPrime[j])
            {
                for(int k=j*j;k<n;k+=j)
                    isPrime[k] = false;

            }
        }

        int cnt=0;
        for(int i=1;i<isPrime.length;i++)
        {
            if(isPrime[i])
                cnt++;
        }
        return cnt;

    }
}
