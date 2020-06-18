#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char const *argv[])
{
    vector<int> arr1{5, 1, 22, 25, 6, -1, 8, 10};
    vector<int> arr2{1, 6, -1, 10};

    int j = 0;

    for (int i = 0; i < arr1.size() && j < arr2.size(); i++)
    {
        if (arr1[i] == arr2[j])
        {
            j++;
        }
    }
    if (j == arr2.size())
    {
        cout << true << endl;
    }
    else
    {
        cout << false << endl;
    }
    return 0;
}
