// 2769_Find_the_Maximum_Achievable_Number.cpp : This file contains the 'main' function. Program execution begins and ends there.

#include <iostream>
using namespace std;

int theMaximumAchievableX(int num, int t) {
    return 2 * t + num;
}


int main()
{
    std::cout << theMaximumAchievableX(10, 2) << endl;
}

