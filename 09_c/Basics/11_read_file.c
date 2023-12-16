# include <stdio.h>

int main(){
    FILE *fPtr = fopen("sample.txt","r");
    int ct = 0;
    char str[100];

    while (fgets(str, 100, fPtr)!= NULL){
        printf("%s", str);
        
    }
    fclose(fPtr);






    return 0;
}