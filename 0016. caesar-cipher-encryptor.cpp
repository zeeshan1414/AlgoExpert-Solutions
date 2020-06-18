#include <iostream>
using namespace std;

string caesarCipher(string str, int key)
{
    char chars[26];
    for (int i = 0; i < 26; i++)
    {
        chars[i] = 97 + i;
    }
    string res = "";
    for (int i = 0; i < str.length(); i++)
    {
        int ch = str[i] - 97;
        ch = chars[(ch + key) % 26];
        res += ch;
    }
    return res;
}

int main(int argc, char const *argv[])
{
    cout << caesarCipher("abc", 2);
    return 0;
}
