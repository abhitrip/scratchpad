#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

vector<string> print_all_substrings_iterative(const std::string& str)
{
    vector<string> strres;
     int size = str.size();
    for (int i = 1; i < (1<<size); ++i) {
        string tmp="";
        for (int j = 0; j < size; ++j) {
            if (i & (1 << j)) {
                tmp+=str[j];
            }
        }
        strres.push_back(tmp);

    }
    return strres;
}



int main()
{
    string s = "abc";
    vector<string> res = print_all_substrings_iterative(s);
    for(int i=0;i<res.size();i++)
        cout<<res[i]<<endl;
    return 0;


}
