# include <stdio.h>
int power(int base, int power);

int main(){
    int b = (int)getchar();
    int p = (int)getchar();
    printf("The ans is: %d", power(b, p));
    return 0;
}


int power(int base, int power){
    for(int i=1; i<power; i++){
        base *= base;
    }
    return base;
}