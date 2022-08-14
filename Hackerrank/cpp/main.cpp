#include<iostream>
using namespace std;

int main(){
    string name = "";
    cin >> name;

    int length = name.length();
    for(int i = 0; i <= length; i++)
    {
        cout << name[length-i];
    }
}