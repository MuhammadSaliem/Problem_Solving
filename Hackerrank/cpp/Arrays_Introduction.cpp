#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n = 0;
    scanf("%d", &n);
    int arr[n];
    
    
    for(int i = 0; i < n; i++){
        int num;
        scanf("%d", &num);
        arr[i] = num;
    }
     
    for(int i = n-1; i >= 0; i--){      
        printf("%d ", arr[i]);
    }
    
    return 0;
}
