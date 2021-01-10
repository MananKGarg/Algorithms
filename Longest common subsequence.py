def lcs(a,b):
    lcs_matrix = [[0 for i in range(len(a)+1)] for j in range(len(b)+1)]
    for i in range(1, len(b)+1):
        for j in range(1, len(a)+1):
            if(a[j-1] == b[i-1]):
                lcs_matrix[i][j] = lcs_matrix[i-1][j-1] + 1
            else:
                lcs_matrix[i][j] = max(lcs_matrix[i-1][j], lcs_matrix[i][j-1])
    return lcs_matrix[-1][-1]

print(lcs("aggtab","gxtxayb"))




