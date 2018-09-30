class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        '''
        logic: make table based on length
        
        
        
        '''
        l = len(s)
        hold = []
        DP = [[-1 for _ in range(l)] for _ in range(l)]
        for substring_length in range(1, l + 1):
            for start in range(0, l - substring_length + 1):
                end = start + substring_length - 1
                substring = s[start: end + 1]
                if substring in wordDict:
                    hold.append(substring)
                    DP[start][end] = start
                    continue

                
                
                for split in range(start+1, end+1):
                    if DP[start][split - 1] != -1 and DP[split][end] != -1:
                        DP[start][end] = split
                        break          
        print(DP)
