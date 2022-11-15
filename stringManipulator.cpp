#include<iostream>
using namespace std;

// function that checks the character
// is in upper case or not
bool isupper(char ch)
{
        if(ch>=65 && ch<=90)
        {
                return true;
        }
        return false;

}

// function that checks the character
// is in upper case or not
bool islower(char ch)
{
        if(ch>=90 && ch<=122)
        {
                return true;
        }
        return false;
}

// function that checks the character
// is a space or not
bool isspace(char ch)
{
        if(ch == 32)
        {
                return true;
        }
        return false;
}


// function that converts the character
// into upper case
char upper(char ch)
{
        if(islower(ch))
        {
                return ch-32;
        }
        return ch;
}

// function that converts the character
// into lower case
char lower(char ch)
{
        if(isupper(ch))
        {
                return ch+32;
        }
        return ch;
}



// function that finds the length of the string
int len(string str)
{
        int l=0;
        for(char x:str)
        {
                l++;
        }
        return l;
}


// converts the string into uppercase
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


// converts the string into lowercase
string tolowercase(string str)
{
        for(int i=0;i<len(str);i++)
        {
                if(isupper(str[i]))
                {
                        str[i] = lower(str[i]);
                }
        }
        return str;
}

// Thsi function converts the string into
// "Capitalize each word" case
string capitalizecase(string str)
{
        for(int i=0;i<len(str)-1;i++)
        {
                if( isspace(str[i]) && islower(str[i+1]) )
                {
                        str[i+1] = upper(str[i+1]);
                }
                else
                {
                       str[i+1] = lower(str[i+1]);
                }
        }
        str[0] = upper(str[0]);
        return str;
}

// This function convert the string in to sentence case
string sentencecase(string str)
{
        for(int i=0;i<len(str);i++)
        {
                if(isupper(str[i]) )
                {
                        str[i] = lower(str[i]);
                }

        }
        str[0] = upper(str[0]);
        return str;
}


// This function toggle the case
// of the character in string
// and returns the string
string togglecase(string str)
{
        for(int i=0;i<len(str);i++)
        {
                if(isupper(str[i]) )
                {
                        str[i] = lower(str[i]);
                }
                else if(islower(str[i]) )
                {
                        str[i] = upper(str[i]);
                }

        }
        str[0] = upper(str[0]);
        return str;
}

// finds out whether the two strings are same or not
bool issame(string a, string b)
{
        if( len(a)!= len(b)) return false;

        for( int i=0; i< len(a); i++)
        {
                if( a[i] != b[i]) return false;
        }
        return true;
}

// reversestr() returns the string into reverse order
string reversestr(string str)
{
        string rev = str;
        for( int i=0; i<len(str); i++)
        {
                rev[i] = str[len(str)-1-i];
        }
        return rev;
}


// This function checks whether the
// string is palindromic or not
bool ispalindromic(string str)
{
        if(issame( str, reversestr(str))) return true;
        return false;

}

// index() function return the first occurrence
// of a given character in a string
// return -1 if not found
int index(string str, char x)
{
        for(int i=0; i<len(str); i++)
        {
                if( str[i] == x)
                {
                        return i;
                }
        }
        return -1;
}


// indexstr() function return the first occurrence
// of a given string in a string
// return -1 if not found
int indexstr(string str, string x)
{
        for(int i=0; i<len(str); i++)
        {
                bool ans = true;
                for( int c=0; c<len(x); c++)
                {
                        if( str[i+c] != x[c]) ans = false;
                }
                if(ans) return i;
        }
        return -1;
}



int main()
{
        string str = "rAm iS a gOOd boy";

        cout<<touppercase(str)<<endl;
        cout<<tolowercase(str)<<endl;
        cout<<capitalizecase(str)<<endl;
        cout<<sentencecase(str)<<endl;
        cout<<togglecase(str)<<endl;

        cout<<reversestr(str)<<endl;
        cout<<issame(str,str)<<endl;

        cout<<ispalindromic(str)<<endl;

        cout<<index(str,'i')<<endl;

        cout<<indexstr(str,"iS")<<endl;


        return 0;
}
