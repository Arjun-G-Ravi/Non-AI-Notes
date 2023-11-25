# include <stdio.h>

struct Node{
    char name[20];
    int age;
};

int main(){
    struct Node s;
    printf("%d",s.age);
    s.age = 10;
    printf("%d",s.age);
    return 0;
}
