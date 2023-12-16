# include<stdio.h>
# include<stdlib.h>
# include<string.h>

typedef struct Node{
    char name[20];
    int age;
}Node;

int main(){

    Node *ptr = (Node *)malloc(sizeof(Node));
    strcpy(ptr->name, "Varun");
    (*ptr).age = 12; // ptr->age is preferred  


    printf("Name: %s\n", ptr->name);
    printf("Age: %d\n", ptr->age);
    printf("Completed\n");
    return 0;
}