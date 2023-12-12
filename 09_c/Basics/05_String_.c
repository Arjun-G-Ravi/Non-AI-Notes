# include <stdio.h>
#include <string.h>

void main(){
    char name[] = "John Wick";
    name[5] = 'K';
    printf("%s\n",name); 
    printf("%ld\n", strlen(name));

    if (strncmp(name, "John Jones", strlen(name)) == 0){ // 0 means that they are equal
        printf("Hello Jon jones/n");
    }
    else{
        printf("Wrong people\n");
    }

}