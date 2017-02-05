#include <iostream>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;
class Solution{
    public:
        string fractionToDecimal(int numerator,int denominator)
        {
            if(numerator==0)
                return "0";
            
            string res="";
            long long n = numerator;
            long long d = denominator;
            if(n<0 ^ d<0)
                res.append("-");
            n = abs(n);
            d = abs(d);

            res.append(to_string(n/d));
            n = n%d;
            if (n)
                res.append(".");
            unordered_map<int,int> map;
            for(;n!=0;n=n%d)
            {   
                if(map.count(n)>0)
                {
                    res.insert(map[n],1,'(');
                    res.append(")");
                    return res;
                }
                map[n] = res.size();
                n = n*10;
                res.append(to_string(n/d));

            }

            return res;

            
        }

};

int main()
{
    Solution *sol = new Solution();
    cout<<sol->fractionToDecimal(1,5);
}