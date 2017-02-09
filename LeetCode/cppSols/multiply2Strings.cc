class Solution {
public:
    string multiply(string num1, string num2) {
        int s1 = num1.size();
        int s2 = num2.size();
        string res(s1+s2,'0');
        for(int i=s1-1;i>=0;i--)
        {
            int carry=0;
            for(int j=s2-1;j>=0;j--)
            {
                int tmp = res[i+j+1]-'0'+(num1[i]-'0')*(num2[j]-'0')+carry; 
                res[i+j+1] = tmp%10+'0';
                carry = tmp/10;
            }
           res[i] += carry; 
        }
        int idx=0;
       size_t startpos = res.find_first_not_of("0");
        if (string::npos != startpos) {
            return res.substr(startpos);
        }
        return "0";
        
        
    }
};