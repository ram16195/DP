class Solution:
    def uniquePaths(self, rows, cols):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = [[0] * rows] * cols
        #print(a)
        a[0] = [1]*(rows)
        for i in a:
            i[0] = 1

        for i in range(1,cols):
            for j in range(1,rows):
                a[i][j] = a[i][j-1] + a[i-1][j]
        print(a)
        '''
        for row in range(1, rows):
            for col in range(1, cols):
                T[row][col] = T[row - 1][col] + T[row][col - 1]
        return T[rows - 1][cols - 1]
'''
