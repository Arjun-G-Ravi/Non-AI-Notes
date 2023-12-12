# include <stdio.h>

void main(){
    char name[20];
    fgets(name,20,stdin);
    printf("Your name is %s", name);
}


