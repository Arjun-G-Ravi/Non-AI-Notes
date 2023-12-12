# include<stdio.h>

void cow(int num){
    static int counter = 0; // Static makes this valid even if many functions are called, which is kind of wierd!
    for (int i=0; i<num; i++){
        counter++;
        printf("%d ", counter);
        printf("Moo\n");
    }
}

void main(){
    cow(10);
    cow(20);
    
}
