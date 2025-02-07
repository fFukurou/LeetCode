#include <iostream>

//int addDigits(int num) {
//    int sum = 0;
//    while (num)
//    {
//        sum += (num % 10);
//        num /= 10;
//    }
//    if (sum < 10)
//        return sum;
//    else
//        return addDigits(sum);
//}


int addDigits(int num)
{
    while (num / 10 != 0)
    {
        int firstNum = num / 10;
        int secondNum = num % 10;

        num = firstNum + secondNum;
        addDigits(num);


    }
    return num;
}



int main()
{
    //std::cout << addDigits(38) << std::endl;
    std::cout << addDigits(38) << std::endl;

}