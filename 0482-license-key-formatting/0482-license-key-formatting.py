class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        count = 0
        ans = ['']
        for i in reversed(range(n)):
            if (s[i] != '-'):
                ans += s[i].upper()
                count = count + 1
                if (count == k):
                    count = 0
                    ans += '-'
     
        # Make sure the output doesn't start with a dash
        if (len(ans) > 0 and ans[len(ans)-1] == '-'):
            ans = ans[:-1]
        ans = ans[::-1]
        result = "".join(ans)
        return result