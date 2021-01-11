def edit_distance(s,t):                          # converting s to t
    matrix = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]

    for i in range(1, len(t)+1):
        matrix[0][i] = 1                         # edit distance between 1 character and 0 character is 1
    for j in range(1, len(s)+1):
        matrix[j][0] = 1

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i-1] == t[j-1]:                 # if the last character is same, no additional step is required
                matrix[i][j] = matrix[i-1][j-1]
            else:
                replace = 1 + matrix[i-1][j-1]   # replace the last character of s with t
                insertion = 1 + matrix[i-1][j]   # insert a character at the end of t
                deletion = 1 + matrix[i][j-1]    # delete a character at the end of t
                matrix[i][j] = matrix[i][j] + min(replace, insertion, deletion)
    return matrix[-1][-1]

print(edit_distance('food','money'))
