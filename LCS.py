
def lcs(s1,s2):
    rows = len(s1)+1
    cols = len(s2)+1
    T = [ [0 for _ in range(rows)] for _ in range(cols)]
    maxlen = 0
    for i in range(1,rows):
        for j in range(1,cols):
            if(s1[i-1] == s2[j-1]):
                T[i][j] = T[i-1][j-1]+1
            else:
                T[i][j] = max(T[i][j-1],T[i-1][j])
    maxlen = max(maxlen,T[-1][-1])
    return maxlen
print(lcs('abc','abe'))
