#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

void reverse(char word[],int start,int end)
{
    // Reverse Logic
    while(start<end)
    {
        char tmp = word[start];
        word[start] = word[end];
        word[end] = tmp;
        start++;
        end--;
    }
}

bool findNext(char word[],int len)
{
    int i=0;
    if(len<2)
        return false;

    int chngIdx = -1;

    // Find first position where the array is in increasing order
    for(i=len-2;i>=0;i--)
    {
        if(word[i]<word[i+1])
        {

            chngIdx = i;
            break;
        }
    }
    if(chngIdx==-1)
        return false;

    // Now find first character to right of chngIdx greater than it
    for(i=len-1;i>chngIdx;i--)
    {
        if(word[i]>word[chngIdx])
        {
            break;
        }
    }


    if(chngIdx==0 && i==0)
    {
        reverse(word,0,len-1);
        return true;
    }

    else
    {
        // Swap the chngIdx word and next greater word
        char tmp = word[chngIdx];
        word[chngIdx] = word[i];
        word[i] = tmp;

        reverse(word,chngIdx+1,len-1);
        return true;


    }






}

int main()
{


    char digits[] = "ecdigf";
    int n = strlen(digits);
    findNext(digits, n);
    cout<<digits;

    return 0;



}
