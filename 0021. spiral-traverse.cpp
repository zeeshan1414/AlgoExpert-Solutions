#include <iostream>
#include <vector>
using namespace std;

void print(const vector<vector<int>> &arr)
{
    for (int i = 0; i < arr.size(); i++)
    {
        for (int j = 0; j < arr[i].size(); j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}

vector<int> spiralTraverse(const vector<vector<int>> &vect)
{
    vector<int> v;
    if (vect.empty())
        return {};
    int startRow = 0;
    int endRow = vect.size() - 1;
    int startCol = 0;
    int endCol = vect[0].size() - 1;
    int dir = 0;
    while (startCol <= endCol and startRow <= endRow)
    {
        switch (dir)
        {
        case 0:
            for (int col = startCol; col <= endCol; col++)
                v.push_back(vect[startRow][col]);
            startRow += 1;
            break;
        case 1:
            for (int row = startRow; row <= endRow; row++)
                v.push_back(vect[row][endCol]);
            endCol -= 1;
            break;
        case 2:
            for (int col = endCol; col >= startCol; col--)
                v.push_back(vect[endRow][col]);
            endRow -= 1;
            break;
        case 3:
            for (int row = endRow; row >= startRow; row--)
                v.push_back(vect[row][startCol]);
            startCol += 1;
            break;
        }
        dir = (dir + 1) % 4;
    }
    return v;
}

int main(int argc, char const *argv[])
{
    vector<vector<int>> vect{{1, 2, 3, 4},
                             {5, 6, 7, 8},
                             {9, 10, 11, 12}};
    print(vect);
    vector<int> v = spiralTraverse(vect);
    for (int i : v)
        cout << i << " ";
    return 0;
}
