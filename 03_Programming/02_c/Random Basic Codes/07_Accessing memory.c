# include <stdio.h>

int main(){

    int cow = 10;

    printf("%p\n", &cow);
    printf("%ld\n", &cow); // Its decimal counterpart, except it creates a warning.

    // make a ptr for cow
    int *pCow = &cow;
    printf("Cow: %p\n", pCow);
    printf("*Cow: %d\n\n\n", *pCow);
    return 0;
}