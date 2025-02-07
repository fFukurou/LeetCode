#include <iostream>
#include <set>
#include <vector>
#include <unordered_map>

using namespace std;

int firstUniqChar(string s) {
    unordered_map<char, int> mp;

    for (auto a : s) 
    {
        mp[a]++;
    }
    for (int i = 0; i < s.size(); i++)
    {
        if (mp[s[i]] == 1)
        {
            return i;
        }
    }
    return -1;
}


int main()
{
    cout << firstUniqChar("aabb") << endl;
    /*std::cout << "Hello World!\n";*/
}
