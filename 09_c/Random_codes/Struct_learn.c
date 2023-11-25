# include <stdio.h>

struct Node{
    char name[20];
    int age;
};

int main(){
    struct Node s;
    s.age = 10;
    printf("%d",s.age);
    s.name = "John";
    printf("%s", s.name);
    return 0;
}
