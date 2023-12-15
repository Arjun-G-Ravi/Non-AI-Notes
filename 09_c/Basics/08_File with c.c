# include <stdio.h>

int main(){
    FILE *fPtr = fopen("cow.txt", "w");

    fprintf(fPtr, "Cow is awesome");
    fclose(fPtr);


    return 0;
}