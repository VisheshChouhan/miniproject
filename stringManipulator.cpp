#include<iostream>
using namespace std;


bool isupper(char ch)
{
        if(ch>=65 && ch<=90)
        {
                return true;
        }
        return false;

}

bool islower(char ch)
{
        if(ch>=90 && ch<=122)
        {
                return true;
        }
        return false;
}

char upper(char ch)
{
        if(islower(ch))
        {
                return ch-32;
        }
        return ch;
}

int len(string str)
{
        int l=0;
        for(char x:str)
        {
                l++;
        }
        return l;
}


string touppercase(string str)
{
        for(int i=0;i<len(str);i++)
        {
                if(islower(str[i]))
                {
                        str[i] = upper(str[i]);
                }
        }

        return str;


}









int main()
{
        string str = "ram";

        cout<<touppercase(str);


        return 0;
}
