class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        print(s)
        anti = ''
        
        for i in s:
            d = i[::-1]
            dd = ''.join(d)+" "
            print(dd)
            anti = anti+dd
        return anti.rstrip()
