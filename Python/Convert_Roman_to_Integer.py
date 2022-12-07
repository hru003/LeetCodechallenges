"""Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4."""

def romanToInt(s):
     """
     :type s: str
     :rtype: int
     """
     d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
     out = 0
     for i in range(0,len(s)):
          if i < len(s)-1:
               if d[s[i]] >= d[s[i+1]]:
                    out+=d[s[i]]
               else:
                    out = out - d[s[i]]
          else:
               out += d[s[i]]

     return out

s='MCMXCIV'
romanToInt(s)
