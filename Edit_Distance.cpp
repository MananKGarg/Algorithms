#include <iostream>
#include <string>
using namespace std;

int min(int x, int y, int z){                          // returns minimum of 3 numbers
    if (x <= y && x <= z){
        return x;
    }    
    else if (y <= x && y <= z){
        return y;
    }
    else{
        return z;
    }
}

int edit_distance(string s, string t){                // converting s to t
    int matrix[s.length() + 1][t.length() + 1];
    
    matrix[0][0] = 0;
    for(int i = 1; i <= s.length(); i++){             // edit distance between 1 character and 0 character is 1
        matrix[i][0] = 1;
    }
    for(int j = 1; j <= t.length(); j++){
        matrix[0][j] = 1; 
    }
    
    for (int i = 1; i <= s.length(); i++){
        for (int j = 1; j <= t.length(); j++){
            if (s[i-1] == t[j-1]){                    // if the last character is same, no additional step is required
                matrix[i][j] = matrix[i-1][j-1];
            }
            else{
                int replace{};
                int insertion{};
                int deletion{};
                
                replace = 1 + matrix[i-1][j-1];       // replace the last character of s with t
                insertion = 1 + matrix[i-1][j];       // insert a character at the end of t
                deletion = 1 + matrix[i][j-1];        // delete a character at the end of t                
                matrix[i][j] = min(replace, insertion, deletion);
            }
        }
    }
    return matrix[s.length()][t.length()];
}

int main(){
    string s = "food";
    string t = "money";
    
    cout << edit_distance(s,t);
}
