#include <stdio.h>

int power(int base, int pow);

int main() {
    int b, p;

    printf("Enter base: ");
    scanf("%d", &b);

    printf("Enter power: ");
    scanf("%d", &p);

    printf("OUT: %d%d\n", b, p);
    printf("The ans is: %d\n", power(b, p));

    return 0;
}

int power(int base, int pow) {
    int num = 1;

    for (int i = 0; i < pow; i++) {
        num *= base;
    }

    return num;
}