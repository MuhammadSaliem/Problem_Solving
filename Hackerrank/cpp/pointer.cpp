// https://www.hackerrank.com/challenges/c-tutorial-pointer/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#include <stdio.h>
#include <cmath>

void update(int *a,int *b) {
    int tempA= *a;
    *a = *a + *b;
    *b = abs(tempA - *b);
    // Complete this function    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
