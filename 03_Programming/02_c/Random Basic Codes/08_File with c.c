# include <stdio.h>

int main(){
    FILE *fPtr = fopen("cow.txt", "w");
    fprintf(fPtr, "Cow is awesome\nCow is great\nCow is cow.");
    fclose(fPtr);


    FILE *fPtr2 = fopen("cow.txt", "r");
    char line[100];

    fgets(line,100, fPtr2);
    printf("%s\n", line);

    fgets(line,100, fPtr2);
    printf("%s\n", line);

    return 0;
}