#include <iostream>
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> x;
    for(int i=0;i<10;i++)
        x.push_back(rand()%10);
    sort(x.begin(),x.end(),[](const int &r,const int &l){
        return l<r;
    });

    for(auto &num:x)
        std::cout<<num;
}