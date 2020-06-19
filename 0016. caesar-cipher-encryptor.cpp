#include <iostream>
using namespace std;

// Implementation with capital case and special characters
string caesarCipher(string str, int key)
{

    char capitals[26];
    char smalls[26];

    for (int i = 0; i < 26; i++)
    {
        capitals[i] = i + 65;
    }

    for (int i = 0; i < 26; i++)
    {
        smalls[i] = i + 97;
    }

    string s = "";

    for (char c : str)
    {
        if (isalpha(c))
        {
            char ch;
            if (islower(c))
            {
                ch = smalls[(c - 19 + key) % 26];
            }
            else if (isupper(c))
            {
                ch = capitals[(c - 13 + key) % 26];
            }
            s += ch;
        }
        else
        {
            s += c;
        }
    }

    return s;
}

string caesarCipherIgnoreCase(string str, int key)
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
