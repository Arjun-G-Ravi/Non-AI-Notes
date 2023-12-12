# include <stdio.h>

void main(){
    int mat[3][2] = {{1,2}, {3,4}, {5,6}};

    for (int i=0; i<3; i++){
        for(int j=0; j<2; j++){
            printf("%d %d", i, j);
            printf("  %d\n", mat[i][j]);
        }
    }

}

