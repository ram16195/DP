'''
How do we find the number of unique bsts.

How do solve this.  This can be thought of in DP.  We need to solve it by deduing the problem as subproblems. 

Unique bsts at n = T = T[i-1]+T[i-j] .  j->1,i+1 ; i>2,n+1




'''


        def soln(self,n):
          G = [0]*(n+1)
          G[0],G[1] = 1,1

          for i in range(2,n+1):
              for j in range(1,i+1):

                  G[i] += G[j-1]*G[i-j]
          print(G)
