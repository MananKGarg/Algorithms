#include <iostream>
#include <cstring>
using namespace std;

int max(int a, int b){
    if (a > b){
        return a;
    }
    else{
        return b;
    }
}

int lcs(char *A, char *B){
    int m = strlen(A);
    int n = strlen(B);
    
    int lcs_matrix[n + 1][m + 1];
    
    for (int i{}; i <=n; i++){
        for (int j{}; j <= m; j++){
            if (i == 0 || j == 0){
                lcs_matrix[i][j] = 0;
            }
            else if (B[i-1] == A[j-1]){
                lcs_matrix[i][j] = lcs_matrix[i-1][j-1] + 1;                    // When last character is same, one character is added to lcs
            }
            else{
                lcs_matrix[i][j] = max(lcs_matrix[i-1][j],lcs_matrix[i][j-1]);  // When its not same, it is maximum of one complete string with one complete string without the last character
            }
        }  
    }
    return lcs_matrix[n][m];
}

int main()
{
    char A[] = "aggtab";
    char B[] = "gxtxayb";
    
    cout << "lcs " << lcs(A,B);
    return 0;
}
